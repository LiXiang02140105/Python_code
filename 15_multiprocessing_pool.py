'''
pool进程池
    如果想启动大量的子进程，就需要使用进程池的概念
'''

from multiprocessing.pool import Pool
import os,time,random

def long_time_task(name):
    print('Run task %s (%s)' % (name,os.getpid()))
    start = time.time()
    print("start : ", start," - ",name)
    time.sleep(random.random(3))
    end = time.time()
    print("end : ", end," - ",name)
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == "__main__":
    print("parent process %s." % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args = (i,))
    print("waiting for all subprocesses done...")
    p.close()
    p.join()
    print("all subprocesses done.")