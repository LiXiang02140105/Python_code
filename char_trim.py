

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