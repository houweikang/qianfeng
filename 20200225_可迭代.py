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
'''