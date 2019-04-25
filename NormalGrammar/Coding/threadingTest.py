import threading
import time
from collections import deque

#------------线程
def worker(num):
    time.sleep(1)
    print("The num is %d" %num)
    return

def create_thread():
    for i in range(20):
        # 创建线程
        t = threading.Thread(target=worker,args=(i,),name="t.%d"%i)
        t.start()

#------------锁
def test_lock():
    globals_num = 0
    lock = threading.RLock()
    for i in range(10):
        t = threading.Thread(target=test_func,args=(i,lock,globals_num,),name="t.%d"%i)
        t.start()

def test_func(num,lock,globals_num):
    lock.acquire()
    globals_num += 1
    time.sleep(1)
    print("This thread is %d"%num)
    print("globals_num:",globals_num)
    lock.release()

#------------事件
def test_event():
    event = threading.Event()
    event2 = threading.Event()
    t = threading.Thread(target=do_event,args=(event,))
    t2 = threading.Thread(target=do_event,args=(event2,))
    t.start()
    t2.start()
    print("They are waiting!")
    flag = True
    while flag:
        inp = input("The thread that you want to unlock and input 'exit' to exit : ")
        if inp=='t':
            event.set()
            print("You have unlocked 't' ")
        elif inp == 't2':
            event2.set()
            print("You have unlocked 't2' ")
        elif inp == 'exit':
            break

def do_event(event):
    print("start")
    event.wait()
    print("end")

#------------condition类
def consumer(cond):
    with cond:
        print("consumer before wait")
        cond.wait()
        print("consumer after wait")
   
def producer(cond):
    with cond:
        print("producer before notifyAll")
        cond.notifyAll() #唤醒所有在等待condition变量的线程
        #cond.notify() #唤醒一个在等待condition变量的线程
        print("producer after notifyAll")
   
def test_condition():
    condition = threading.Condition()
    c1 = threading.Thread(name="c1", target=consumer, args=(condition,))
    c2 = threading.Thread(name="c2", target=consumer, args=(condition,))
    
    p = threading.Thread(name="p", target=producer, args=(condition,))
    
    c1.start()
    time.sleep(2)
    c2.start()
    time.sleep(2)
    p.start()

#------------生产者消费者

        


if __name__ == "__main__":
    # CreateThread()
    # test_lock()
    # test_event()
    test_condition()
