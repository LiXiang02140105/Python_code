'''
文件操作
StringIO & BytesIO
操作文件和目录
序列化
'''
from io import BytesIO

f = BytesIO()

f.write("李翔".encode('utf-8'))

print(f)
print(f.getvalue())

import pickle

d = pickle.loads(f.getvalue())
print(d)
