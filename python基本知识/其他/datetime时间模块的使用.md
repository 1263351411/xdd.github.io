# datetime时间模块
## datetime类,时间模块中的类datetime
* 类方法
    * todaty() 返回本地时区当前时间的datetime对象
    * now(tz==None) 返回当前时间的datetime对象，时间到微妙，如果tz为None，返回和today()一样
    * utcnow()  返回没有时区的当前时间
    * fromtimestamp(timestamp,tz=None)从一个时间戳返回一个datetime对象
        * timestamp  时间戳
        * tz 时区
    * strptime(date_string,format) 将指定格式的字符串转换为datetime对象，【日期的格式化】
        例如：
        ````python 
        datetime.datetime.strptime("2019-04-8 15:18","%Y-%m-%d %H:%M") 
        ````
* datetime对象
    * timestamp()-->int 返回一个到微妙的时间戳。
        * 时间戳：格林威治时间1970年1月1日0点到现在的秒数
    * datetime(year,month,day,hour,minute,second,microsecond)--->datetime 构造方法，创建指定时间
    * weekday() 返回本周的第几天，周一 0  ，周日 6
    * isoweekday() 返回本周的第几天，周一 1  ，周日 7
    * date() 返回日期date对象
    * time() 返回时间time对象
    * replace() 修改并返回新的时间
    * isocalendar() 返回一个三元组(年，周数,一周内的第几天)
    * strftime(format) --->string,将datetime对象转换成指定格式的时间字符串
        例如：
        ````python
        datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        "{0:%Y}-{0:%m}-{0:%d}".format(datetime.datetime.today())
        ```` 
* timedelta对象(时间差)
    * datetime.timedelta(days=0,seconds=0,microseconds=0,milliseconds=0,minutes=0,hours=0,weeks=0)
        * 构造方法
        * timedelta对象还可以根据两个时间相减得到。
            * 例如： timedelta = datetime1 - datetim2
            * 同样datetime加上timedelta可以获取新的datetime对象。则 datetime2 = datetime1 + timedlata
    * total_seconds() 返回时间差的总秒数
* 简单示例：  
````python
import datetime
d1 = datetime.datetime.now() # 获取当前时间
d2 = datetime.datetime.utcnow() # 获取utc时间
d3 = datetime.datetime.today() # 获取当前时间
d4 = datetime.datetime(2019,4,10) # 获取指定时间
print(d1,d2,d3,d4,sep="\n")

d5 = datetime.datetime.fromtimestamp(d4.timestamp()) # 根据d4的时间戳获取datetime对象
d6 = datetime.datetime.fromtimestamp(int(d3.timestamp())) # 根据d3的时间戳（只要秒以前的），获取datetime对象
print(d5,d6,sep="\n")
````
![datetime001](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/datetime001.jpg)  

## 相关库time
* time.sleep(5)  #当前进程休眠5秒
