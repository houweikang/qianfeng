# 匿名函数:简化函数定义
# 格式 lambda 参数1，参数2...： 运算


def func():
    print('---aaa---')


def add1(a, b):
    s = a + b
    return s


add2 = lambda a, b: a + b

print(add1(1, 2))
print(add2(1, 2))

# max(iterator,func):根据func定义的元素 得到最大值  同 min() :
lst1 = [{'a': 10}, {'a': 20}, {'a': 5}]
m = max(lst1, key=lambda x: x['a'])
print(m)

# map(func,iterator) :根据func定义的运算  得到iterator迭代后运算后的元素

lst2 = [1, 2, 3, 5, 7, 6]
#   对列表中的元素*10
result2 = map(lambda x: x * 10, lst2)
print(list(result2))

#   对列表中的奇数进行+1操作
result3 = map(lambda x: x if x % 2 == 0 else x + 1, lst2)
print(list(result3))

# reduce(func,iterator) : 对可迭代对象类型（list,tuple...)中的元素一次累加进行func定义的运算，得到最终值

from functools import reduce

t1 = [3, 6, 7, 5, 9]
result = reduce(lambda x, y: x + y, t1)
print(result)

# filter(func,iterator):根据func定义的功能 筛选出iterator符合的元素

result = filter(lambda x: x > 5, t1)
print(list(result))

# sorted(iterator,func):根据func定义的元素 排列iterator中的元素
lst1 = [{'a': 10}, {'a': 20}, {'a': 5}]
result = sorted(lst1, key=lambda x: x['a'])
print(result)
