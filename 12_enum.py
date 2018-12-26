'''
实现枚举类

'''
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

if __name__ == "__main__":
    for name,member in Month.__members__.items():
        #想把 __memberes__拆分来看，看看里面是什么
        print(name,'=>',member,',',member.value)

