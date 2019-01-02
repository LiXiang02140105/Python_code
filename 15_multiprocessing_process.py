'''
多进程 - Windows
    Python的multiprocessing模块提供了一个Process类来代表一个进程对象
    multiprocessing模块是跨平台版本的多进程模块。

问题：
    安装multiprocessing时，遇到了一个都会遇到的问题
    SyntaxError: Missing parentheses in call to 'print'. Did you mean print(int 'Macros:')?
    原因是python3.x和Python2.x兼容的问题
'''
from multiprocessing.process import BaseProcess
import os

def run_process(name):
    print("子进程为：%s, %s" % (name,os.getpid()))

if __name__ == "__main__":
    print("父进程为： %s" %  os.getpid())
    child = BaseProcess(target = run_process, args = ('test',))
    print("子进程开始！")
    child.start()
    child.join()
    print("子进程结束！")