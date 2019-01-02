'''
datetime中timedelta模块是用来做时间对象的加减法
时间对象的类型：
    datetime:datetime()、datetime.now()
    utc(浮点型):timestamp,分为当地的时间和UTC(0时区)
    str:格式化的输入输出,strptime()、strftime()
'''
from datetime import datetime,timedelta

now = datetime.now()

print("这个是datetime对象\n当前时间为：",now)

#转成格式化的输出
str_time = now.strftime('%Y-%m-%D %H-%M-%S')
print("这个是str对象\n当前时间为：",str_time)

#转成timestamp的输出
stamp_time = now.timestamp()
print("这个是timestamp对象\n当前时间为：",stamp_time)

print("当前时间 {0} 加12个小时是多久 {1}".format(now,now + timedelta(hours = 12)))

print("当前时间 {0} 加一天是多久 {1}".format(now,now + timedelta(days = 1)))

print("当前时间 {0} 加两天8个小时是多久 {1}".format(now,now + timedelta(days = 2, hours = 12)))