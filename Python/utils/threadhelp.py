"""
author:木木夕
date:2019-11-25 14:34
"""
from concurrent.futures import ThreadPoolExecutor
import time

# 多线程异步任务，帮助同步执行。
class ThreadHelp():

    def __init__(self,max_workers:int=5):
        self.__fs__ = []
        self.__executer__ = ThreadPoolExecutor(max_workers=max_workers)

    # 添加需要运行的函数和参数
    def addfunc(self,func,*args):
        self.__fs__.append(self.__executer__.submit(func,*args))

    # 等待全部运行结束
    def run_wait(self,slooptime=2):
        while True:
            time.sleep(slooptime)
            flag = True
            for f in self.__fs__:
                flag = flag and f.done()
            if flag:
                break
        self.__executer__.shutdown(wait=True)


    def __del__(self):
        self.__executer__.shutdown(wait=True)