import functools,datetime,inspect
def xdd_print(pstr:str):
    """
    日志输出方法，需要改进，添加功能。
    :param pstr: 需要输出的字符串
    :return: None
    """
    print(pstr)

class StaticMethod:
    """静态方法装饰器，类似于staticMethod"""
    def __init__(self,fn):
        self.fn = fn

    def __get__(self, instance, owner):
        return self.fn

class ClassMethod:
    """类方法装饰器，类似于classmethod"""
    def __init__(self,fn):
        self.fn = fn

    def __get__(self, instance, owner):
        def _fn(*args,**kwargs):
            return self.fn(owner,*args,**kwargs)
        functools.update_wrapper(_fn,self.fn)
        # return functools.partial(self.fn,owner) #也可以使用偏函数
        return _fn

class Property:
    """自己实现property和Property功能一样"""
    def __init__(self,fn):
        self._fn = fn

    def setter(self,fn):
        self.set = fn
        return self

    def deleter(self,fn):
        self.defn = fn
        return self

    def __delete__(self, instance):
        if hasattr(self,"defn"):
            self.defn(instance)

    def __get__(self, instance, owner):
        return self._fn(instance)

    def __set__(self, instance, value):
        if not hasattr(self,"set"):
            raise AttributeError("can't set attribute")
        self.set(instance,value)


def xdd_time(fn):
    """
    时间统计，统计函数执行时间
    :param fn: 需要装饰的函数
    :return: 包装后的fn
    """
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        start = datetime.datetime.now()
        req = fn(*args,**kwargs)
        timeout = datetime.datetime.now() - start
        xdd_print("{}方法耗时：{}，args={},kwargs={},\n执行结果：req={}".format(fn.__name__,timeout.total_seconds(),args,kwargs,req))
        return req
    return wrapper

class Xdd_Timeit:
    """
    时间统计类，也可以作为装饰器单独统计单个函数运行时长
    """

    def __init__(self,fn):
        """
        初始化方法
        :param fn: 需要统计的函数
        """
        functools.update_wrapper(self,fn)
        self.fn = fn
        self.starttime = None
        self.stoptime = None

    #with语句开始时默认调用的方法
    def __enter__(self):
        self.starttime = datetime.datetime.now()
        return self

    #with语句结束后默认调用的方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stoptime = datetime.datetime.now()
        print("{} 总运行时长：{}".format(self.fn.__name__,(self.stoptime-self.starttime).total_seconds()))

    #使得类对象是个可调用函数
    def __call__(self, *args, **kwargs):
        start = datetime.datetime.now()
        sum = self.fn(*args, **kwargs)
        sound = datetime.datetime.now() - start
        print("{} 运行时长：{}".format(self.fn.__name__,sound.total_seconds()))
        return sum

def xdd_cache(duration = 5):
    """
        为函数生成缓存机制，具有有效时长功能
    :param fn:
    :param duration:缓存时长，单位秒
    :return:
    """
    def _xdd_cache(fn):
        """
            为函数生成缓存机制，具有有效时长功能
        :param fn:
        :param duration:缓存时长，单位秒
        :return:
        """
        xdd_dict = {} #定义一个字典，用来存参数与对应的计算结果
        sig = inspect.signature(fn) #对函数进行签名

        @functools.wraps(fn)
        def wrapper(*args,**kwargs):
            paramestr = getparamestr(args,kwargs) #根据参数获取字符串
            req = xdd_dict.get(paramestr,None)
            if req is None:
                req = fn(*args,**kwargs),datetime.datetime.now()
                xdd_dict[paramestr] = req
            elif (datetime.datetime.now() - req[1]).total_seconds() > duration: #超时
                print("缓存超时")
                req = fn(*args, **kwargs),datetime.datetime.now()
                xdd_dict[paramestr] = req
            return req[0]

        def getparamestr(args,kwargs)->str:
            """
             格式化参数，将参数格式化为指定格式的字符串
            :param args:
            :param kwargs:
            :return:
            """
            parames = sig.parameters
            pstr = ()
            isargs = True #标记是否还有位置参数
            kwdict = {}
            for k,(name,v) in enumerate(parames.items()):
                v:inspect.Parameter = v
                if name == "args": #位置参数已经全部匹配完成
                    isargs = False
                    pstr += ("args",tuple(args[k+1:])) #记录剩下的位置参数
                    continue
                if name == "kwargs": #关键字位置参数已经匹配完
                    pstr += ("kwargs",tuple((k,kwargs[k]) for k in kwargs.keys()-kwdict.keys()))
                    break
                if isargs:  # 位置参数还没匹配完
                    if k<len(args):
                        pstr += (name, args[k])
                    else: #实际传参中位置参数已经传完
                        kwval = kwargs.get(name,v.default)
                        kwdict[name] = kwval  # 记录已经出现的位置参数
                        pstr += (name,kwval)
                else:
                    kwval = kwargs.get(name, v.default)
                    kwdict[name] = kwval #记录已经出现的位置参数
                    pstr += (name,kwval)
                # print(k,name,v.name,v.annotation,v.default)
            return pstr
        return wrapper
    return _xdd_cache

def xdd_paramCheck(fn):
    """
        参数检查
    :param fn:  需要检查的函数
    :return: 包装后的fn
    """
    @functools.wraps(fn)
    def _xdd_paramCheck(*args,**kwargs):
        params = inspect.signature(fn).parameters #对函数签名，获取参数注解字典
        for ag,(k,v) in zip(args,params.items()): ##检查位置参数
            v:inspect.Parameter = v #利用参数注解，告诉编译器v是Parameter类型。本行可以删除，只是帮助编译器给出提示
            # print(k=="args")
            if k == "args": break #如果碰到args收集多个位置参数，就直接跳出循环。
            if v.annotation != inspect._empty and not isinstance(ag,v.annotation):
                # raise TypeError(""{}={},参数类型错误！错误类型：{}，类型应为：{}".format(k,ag,type(ag),v.annotation))
                print("{}={},参数类型错误！错误类型：{}，类型应为：{}".format(k,ag,type(ag),v.annotation))
                return
        for k,v in kwargs.items():
            key:inspect.Parameter = params[k] #利用参数注解，告诉编译器key是Parameter类型。本行可以删除，只是帮助编辑器能给出提示
            if key.empty != key.annotation and not isinstance(v,key.annotation):
                # raise TypeError("{}={},参数错误！错误类型：{}类型应为：{}".format(k,v, type(v),key.annotation))
                print("{}={},参数错误！错误类型：{}类型应为：{}".format(k,v, type(v),key.annotation))
                return
        return fn(*args,**kwargs)
    return _xdd_paramCheck

class Xdd_DataInject:
    """类型检查，可以帮助类实例化时进行类型检查"""
    def __new__(cls, clsto):
        sig = inspect.signature(clsto)
        params = sig.parameters
        for name,param in params.items():
            # print(name,param.name,param.kind,param.default,param.annotation)
            if param.annotation != param.empty:
                setattr(clsto,name,Xdd_DataInject._TypeCheck(name,param.annotation))
        return clsto

    class _TypeCheck:
        """内部内，帮忙解决类型检查"""
        def __init__(self, name, typ):
            self.name = name
            self.typ = typ

        def __get__(self, instance, owner):
            if instance:
                return instance.__dict__[self.name]

        def __set_name__(self, owner, name):
            self.name = name

        def __set__(self, instance, value):
            if isinstance(value, self.typ):
                instance.__dict__[self.name] = value
            else:
                raise TypeError("类型错误{}的类型必须是{}".format(self.name, self.typ))

class Xdd_Fib:
    """
    斐波拉契数列类，获取第num个位置的斐波拉契数列。
    """
    def __init__(self):
        self.fib = [0,1,1]

    def __len__(self):
        return len(self.fib)

    #类的实例可调用
    def __call__(self,num:int):
        if not isinstance(num,int):
            raise TypeError("num必须是int类型")
        if num<0:
            raise KeyError("选项错误，必须大于0")
        elif num<3:
            return self.fib[num]
        else:
            for i in range(len(self),num + 1):
                self.fib.append(self.fib[i-1]+self.fib[i-2])
        return self.fib[num]

    #类可迭代
    def __iter__(self):
        return iter(self.fib)

    def __repr__(self):
        return ",".join(map(str,self.fib))

    __str__ = __repr__
    __getitem__ = __call__ #类可以像数组一样访问


