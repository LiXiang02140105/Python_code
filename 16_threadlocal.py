'''
threadlocal
    作用，就是给每一个线程都能够获取到本线程的参数（局部）
    而不用定义一个全局的变量来存储这些参数
'''
import threading
#创建全局的ThreadLocal对象
local_school = threading.local()


def process_student():
    #比较通过threadlocal控制的参数 args
    #以及在创建threa的时候，每个thread就自带的属性
    std_name = local_school.student
    print('Hello, {0} (in {1})'.format(std_name, threading.current_thread().name))


def process_thread(name):
    #args 是会传入到创建线程的函数(target)中
    #绑定ThreadLocal的student
    local_school.student = name
    process_student()    

if __name__ == "__main__":
    t1 = threading.Thread(target = process_thread, args = ('Alice',), name = "Thread-A")
    t2 = threading.Thread(target = process_thread, args = ('Bob',), name = "Thread-B")
    t1.start()
    t2.start()
    t1.join()
    t2.join()