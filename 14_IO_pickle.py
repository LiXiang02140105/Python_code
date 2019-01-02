'''
序列化 - 变量从内存中变成可存储或传输的过程
    ==>> 为了保存 变量 的更改？
    https://blog.csdn.net/taiyangdao/article/details/79298447
'''

import pickle

d = {
    'name' : "Bob",
    'age' : 20,
    'score' : 88
}
print(d)

pd = pickle.dumps(d)

print(pd)

with open("./test_file/pickle_test.txt","wb+") as f:
    f.write(pd)
    f.close()

with open("./test_file/pickle_test.txt","rb") as f:
    print(str(f.read()))
