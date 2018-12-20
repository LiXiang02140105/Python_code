'''
说明：清除字符串中的空格 - Python有自带的strip()
    1.strip()：把头和尾的空格去掉
    2.lstrip()：把左边的空格去掉
    3.rstrip()：把右边的空格去掉
    4.replace('c1','c2')：把字符串里的c1替换成c2。
                故可以用replace(' ','')来去掉字符串里的所有空格
    5.split()：通过指定分隔符对字符串进行切片，
                如果参数num 有指定值，则仅分隔 num 个子字符串

'''
def trim(s):
    #首先,把字符串转成数组
    origin_s = []
    for char in s:
        if(char != ' '):
            origin_s.append(char)
    res_s = ''.join(origin_s)

    return res_s


if __name__ =="__main__":
    org_s = input('请输入字符串: ')
    print('字符串长度为：',len(org_s))
    res_s = trim(org_s)
    print(res_s,'字符串长度为：',len(res_s))