'''
返回函数
    高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

闭包的知识
    也就是直接早

实际上，是因为在Python中，函数名 f 只是一个变量，相当于C中的指针，指向的是函数 f() 的存储位置
而，之后通过 是使用 f 还是 f()来知道是得到函数的地址还是函数计算之后的值
strip()

'''

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        print("f : ",f,f())
        fs.append(f)
        print("fs[{}]".format(i-1),fs[i-1])
    return fs
    
def count1():
    fs = []
    for i in range(1, 4):
        def f1():
            return i*i
        print("f1 : ",f1,f1())
        fs.append(f1())
        print("fs1[{}]".format(i-1),fs[i-1])
    return fs

if __name__ == "__main__":
    f1,f2,f3 = count()
   
    f4,f5,f6 = count1()
    print("f1 : ",f1,f1())
    print("f2 : ",f2,f2())
    print("f3 : ",f3,f3())
    print("--------------")
    print("f4 : ",f4)
    print("f5 : ",f5)
    print("f6 : ",f6)
