'''
    实现sorted()对一组tuple表示学生名字和成绩进行排序
    https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318230588782cac105d0d8a40c6b450a232748dc854000
    Python2 和 Python3的sorted()出现了较大的改动
        def sorted(iterable, key, reverse)
    
'''
from operator import itemgetter

def by_name(t):
    return t[0]

def by_name1(t1, t2):
    return t1[0] - t2[0]

if __name__ == "__main__":
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    L2 = sorted(L,key=itemgetter(0),reverse=True)
    print(L2)
    L3 = sorted(L, key = lambda x : x[1])
    print(L3)