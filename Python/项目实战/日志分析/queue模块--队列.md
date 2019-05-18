@[toc]
# queue模块--队列
导入方法 ````from queue import Queue````  
## 常用方法
* queue.Queue(maxsize=0)->Queue #创建FIFO队列，返回Queue对象
    * maxsize小于等于0，队列长度没有限制
* Queue.get(block=Tue,timeout=None) #从队列中移除一个元素并返回这个元素。
    * block 为阻塞，timeout为超时。
        * True 是阻塞，timeout为None就是一直阻塞。如果timeout有值，就阻塞到一定秒数抛出Empty异常。
        * false 是非阻塞，timeout将被胡烈，要么成功返回一个元素，要么抛出empty异常
    * timeout 阻塞状态时的超时时间
* Queue.get_nowait() #不阻塞，没有数据立即抛出异常
* Queue.put(item，block=Tuue,timeout=None) #把一个元素添加到队列中去
    * item 需要添加的元素
    * block 阻塞 值如下
        * True 如果timeout为None，则一直阻塞直至有空位置放入新的元素。如果timeout有值，即阻塞对应时间后抛出Full异常
        * False 不阻塞，timeout失效。立即返回。能塞进去就塞，不能则抛出Full异常
````python
# Queue测试 
from queue import Queue 
import random
q = Queue()
q.put(random.randint(1,100)) 
q.put(random.randint(1,100))
 
print(q.get()) 
print(q.get()) 
#print(q.get()) # 阻塞 
#print(q.get(timeout=3)) # 阻塞，但超时抛异常 
#print(q.get_nowait()) # 不阻塞，没数据立即抛异常
````
* **注意**：Queue的数据一旦被get后，就会从队列中消失