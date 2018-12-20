'''
说明：
    需要找到list中的min 和 max，使用元组返回(min,max)
'''

def findMinAndMax(testlist):
    if testlist == []:
        return (None, None)
    
    min = testlist[0]
    max = min
    for i in testlist:
        if i < min:
            min = i
        elif i >= max:
            max = i
    return (min,max)

if __name__ == "__main__":
    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')

isinstance