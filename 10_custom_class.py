'''
定制类
    看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，
    这些在Python中是有特殊用途的
'''
class Student(object):
    def __init__(self,name):
        '''
        __init__是构造函数，即我们new一个对象的时候，就会调用这个函数
        '''
        self._name = name
    
    # def __str__(self):
        '''
        __str__是当执行 Student('Michael') 的时候，会
        '''

if __name__ == "__main__":
    '''
    我有个疑问：
        是不是 obj = class("name")
        obj 和 class("name") 本来都是一个对象，
        而 obj 指向的是 class("name") 对象
    '''
    Michael = Student("Michael")
    
    print("Michael : ",Michael,type(Michael))
    print("Michael init : ",Michael.__init__)
    print("---------\n")
    print("Student(\"Michael\") : ",Student("Michael"))
    print("Student(\"Michael\") init : ",Student("Michael").__init__)
    print("---------\n")
    print("Student: ",Student)
    print("Student init : ",Student.__init__)