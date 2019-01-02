'''
菜鸡准备写个正则表达式：
之前有个考官，让我写如何用正则表达式来定位页面中获取的网址，然后看能不能通
先不写这个
因为我写不出，hhh
写个简单的

请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
    someone@gmail.com
    bill.gates@microsoft.com
'''

import re

def re_match(email):
    #email_match = re.compile(r'^([a-zA-Z]\w*|\w*\.\w*|\w*\_\w*\@\w+\.com)')
    email_match = re.compile(r'^([a-zA-Z][0-9a-zA-z\.\_]*\@\w+\.com)')
    result = email_match.match(email)
    if result != None:
        print('匹配成功：',result.groups())
    else:
        print("无法匹配：",email)

if __name__ == "__main__":
    email = ['someone@gmail.com',\
            'bill.gates@microsoft.com',\
            'bob#example.com',\
            'mr-bob@example.com'
            ]
    i = 0
    while(i < 4):
        re_match(email[i])
        i = i + 1