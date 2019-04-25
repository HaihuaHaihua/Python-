from multiprocessing import Process
from multiprocessing import Array,Value
#-----------进程创建
def create_process():
    p = Process(target=hello,args=("Haihua",))
    p1 = Process(target=hello,args=("WangHaihua",))
    p.start()
    p1.start()
    # p.join() 逐个执行进程 使得不并发

def hello(name):
    print("hello, ",name)

#-----------进程数据共享 Array Value   
def process_share():
    num = Value('d',1.1) #第一个参数 'd'表示数据类型 为double
    arr = Array('i',range(11)) #第一个参数 'i'表示数据类型 为整型
    display_sharedata(num,arr)
    a = Process(target = changedata,args=(num,arr) )
    b = Process(target = changedata,args=(num,arr) )
    a.start()
    b.start()
    a.join()
    display_sharedata(num,arr)
    b.join()
    display_sharedata(num,arr)
    
    

def changedata(num,arr):
    num.value = 0.0
    for i in range(len(arr)):
        arr[i] += 1         

def display_sharedata(num,arr):
    print("the value : ",num.value)
    print("the array : ",end='')
    for i in arr:
        print(i,end=' ')
    print()

#-----------进程数据共享 Manager   
from multiprocessing import Manager

def f(d,l):
    d["name"] = "zhangyanlin"
    d["age"] = 18
    d["Job"] = "pythoner"
    l.reverse()
  
def process_manager():
    with Manager() as man:
        d = man.dict()
        l = man.list(range(10))
  
        p = Process(target=f,args=(d,l))
        p.start()
        p.join()
  
        print(d)
        print(l)

#--------------进程池
from multiprocessing import Pool
import time

def func_apply(i):
    time.sleep(1)
    print("I recieved %d"%i)
    return i + 100

def pool_apply():
    pool = Pool(5)
    for i in range(1,20):
        pool.apply(func=func_apply,args=(i,))
    pool.close()
    pool.join()    

def func_callback(arg):
    print("the arg is %d"%arg)
    
def pool_apply_async():
    pool = Pool(5)
    for i in range(1,20):
        pool.apply_async(func=func_apply,args=(i,),callback=func_callback)
    pool.close()
    pool.join()

if __name__ == "__main__":
    # create_process()
    # process_share()
    # process_manager()
    pool_apply()
#     pool_apply_async()
