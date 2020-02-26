# generateor：生成器

# 1.列表推导式
g = (x * 3 for x in range(10))

#   方式1：__next__()
print(g.__next__())
print(g.__next__())
print(g.__next__())

#   方式2：next(生成器对象)
print(next(g))
print(next(g))
print(next(g))


# 2.函数 含有yield，则为生成器
def func():
    n = 0
    while True:
        n += 1
        yield n  # return n  +  暂停


g2 = func()
print(next(g2))
print(next(g2))


# 斐波那契数列
def fib(length):
    a, b = 1, 1
    n = 0

    while n < length:
        # print(b)
        yield a
        a, b = b, a + b
        n += 1

    return '没有更多元素了...'  # 可返回错误提示 StopIteration: 没有更多元素了...


g3 = fib(8)

while True:
    print(next(g3))

'''
生成器：generator

定义生成器方式：
1.通过列表推导式方式
    g = (x+1 for x in range(10))
2.函数+yield
    def func():
        ...
        yield
    
    g=func()

产生元素：
    1.next(g) --->每次调用都会产生一个元素，若元素产生完毕，再调用就会产生异常
    2.生成器自己的方法：
        g.__next__()
        g.send(value) #第一次要送None
        
应用：协程
'''
