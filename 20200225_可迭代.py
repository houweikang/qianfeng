'''
可迭代对象：
1.生成器
2.元组、列表、集合、字典、字符串
'''

# 判断是否可迭代
from collections.abc import Iterable

l1 = [1, 2, 3, 5]
f = isinstance(l1, Iterable)
print(f)

f = isinstance('abcd', Iterable)
print(f)

g=(x for x in range(10))
f = isinstance(g, Iterable)
print(f)


'''
迭代器：可以被next()函数调用并不断返回下一个值的对象 ---Iterator
特点：
1.从第一个元素访问，知道所有元素被访问完毕
2.只能往前不能后退

生成器是迭代器
列表、元组，字典，集合、字符串不是迭代器，但可以通过iter()变成迭代器
'''

l1 = [1,2,3]
l1 = iter(l1)
print(next(l1))
print(next(l1))