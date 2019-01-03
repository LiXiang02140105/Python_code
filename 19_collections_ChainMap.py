'''
collections是Python内建的一个集合模块，提供了许多有用的集合类
    namedtuple
    deque - 除了实现list的append()和pop()外，还支持appendleft()和popleft()
    defaultdict - 当dict中没有某项key的时候，之前会报错成KeyError，但defaultdict对象给了一个默认值'N/A'
    OrderedDict - 把dict中key的位置固定
    ChainMap - 把dict组装成新的dict
'''

from collections import ChainMap
import os, argparse

#构造缺省参数
defaults = {
    'color' : 'red',
    'user' : 'guest'
}


#构造命令行参数
#parse：解析
#parser：解析器
parser = argparse.ArgumentParser()
parser.add_argument('-c','--color')
parser.add_argument('-u','--user')
namespace = parser.parse_args()
'''
这个if v 我看了很久
才看明白，原来是当有输入color或者user的时候，才会加入到command_line_args
'''
command_line_args = {k:v for k,v in vars(namespace).items() if v}

#组合成ChainMap
combined = ChainMap(command_line_args, os.environ, defaults)

print("color = %s" % combined['color'])
print("user = ",combined['user'])