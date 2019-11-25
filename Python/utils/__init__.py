"""
author:xdd
date:2019-10-11 12:54
"""
from .threadhelp import ThreadHelp

# 筛选所需要的字段
def jsonify(instance,allow=None,exclude=[],asname:dict=None):
    # allow优先，如果有，就使用allow指定的字段，这时候exclude无效
    # allow如果为空，就全体，但要看看有exclude中的要排除
    modelcls = type(instance)
    if allow:
        fn = (lambda x:x.name in allow)
    else:
        fn = (lambda x:x.name not in exclude)
    # from django.db.models.options import Options
    # m:Options = modelcls._meta
    # print(m.fields,m.pk)
    # print("----------")
    if asname:
        return {asname.get(k.name):getattr(instance,k.name) for k in filter(fn,modelcls._meta.fields)}
    return {k.name:getattr(instance,k.name) for k in filter(fn,modelcls._meta.fields)}

#判断字符是否为空
def isNotEmpty(stt:str):
    """
    判断是否为空字符,不为空返回true，为空返回false
    :param stt:
    :return:
    """
    if stt==None or stt=="":
        return False
    elif stt:
        return True
    else:
        return False

#判断是否包含中英文
def is_contain_chinese(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    if check_str:
        for ch in check_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False
    return False

#帮助获取分页
def validate(d:dict,name:str,type_func,default,validate_func):
    """
    帮助获取分页
    :param d: 指定字段的所在对象
    :param name: 需要取出的字段名
    :param type_func: 数据类型
    :param default: 如果找不到，默认取出的值,也是默认最大值
    :param validate_func: 赛选条件
    :return:
    """
    try:
        ret = type_func(d.get(name,default))
        ret = validate_func(ret,default)
    except:
        ret = default
    return ret


