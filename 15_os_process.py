'''
多进程：
    进程是系统资源分配的基本单位
    利用里Python自带的os模块来调用fork()出子进程
    但是由于Windows没有fork调用，下面的代码在Windows上无法运行。
    由于Mac系统是基于BSD（Unix的一种）内核。
Python的os模块封装了常见的系统调用
'''

import os

print(('Process (%s) start. 父进程.' % os.getpid()))

#只在Linux/Unix/Mac中可以实现
pid = os.fork() 

if pid == 0:
    #父进程
    print("这个是父进程，进程号为{0}，它的父进程为守护进程：{1}".format(os.getpid(),os.getppid()))
else:
    #子进程
    print("这个是子进程，进程号为{0}，它的父进程为：{1}".format(os.getpid(),os.getppid()))

    
