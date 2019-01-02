'''
为了匹配邮箱中出现的名字
    <Tom Paris> tom@voyager.org => Tom Paris
    bob@example.com => bob
我以为廖老师的意思是邮箱地址中出现名字的都需要匹配，搞得我很难受hhh
'''
import re

def get_name(email):
    if re.match(r'<',email):
        #如果有 <
        email_match = re.compile(r'^<([a-zA-Z]+\s[a-zA-Z]+)>\s[a-zA-Z]+\@[a-zA-Z]+\.[a-zA-Z]+')
        result = email_match.match(email).group(1)
    else:
        email_match = re.compile(r'^([a-zA-Z]+)\@[a-zA-Z]+\.[a-zA-Z]+')
        result = email_match.match(email).group(1)
    if result:
        print('匹配成功：',result)
    else:
        print("无法匹配：",email)

if __name__ == "__main__":
    email = ['<Tom Paris> tom@voyager.org',\
            'bob@example.com'
            ]
    i = 0
    while(i < 2):
        get_name(email[i])
        i = i + 1