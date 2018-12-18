
test_tuple = (1,2,3,4,5,6)
#测试
print(isinstance(1,int))

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [L.lower() for L in L1 if isinstance(L,str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')