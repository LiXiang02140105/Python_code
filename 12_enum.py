'''
实现枚举类

'''
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

if __name__ == "__main__":
    '''
    Enum中的__members__就是一个特殊的方法
    '''
    '''@property
    def __members__(cls):
        """Returns a mapping of member name->value.
        This mapping lists all enum members, including aliases. Note that this
        is a read-only view of the internal mapping.
        """
        return MappingProxyType(cls._member_map_)
    返回成员名称 - >值的映射。
         此映射列出了所有枚举成员，包括别名。 请注意这一点
         是内部映射的只读视图。
    '''
    ''''
        enum_class._member_map_ = OrderedDict()      # name->value map
    ''''
    for name,member in Month.__members__.items():
        #想把 __memberes__拆分来看，看看里面是什么
        print(name,'=>',member,',',member.value)
    for name,member in Month.__members__:
        print(name,'=>',member,',',member.value)

