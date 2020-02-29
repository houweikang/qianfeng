# time模块

# 1.时间戳
import time

t = time.time()
print(t)

# time.sleep(3)
# t1 = time.time()
# print(t1)

# 将时间戳转成字符串
s = time.ctime(t)
print(s)

# 将时间戳转成元组
t2 = time.localtime(t)
print(t2)

# 将元组转成时间戳
tt = time.mktime(t2)
print(tt)

#将时间转成字符串
print(time.strftime('%Y/%m/%d'))

