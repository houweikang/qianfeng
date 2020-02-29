# 属性
name = 'calculate'


# 函数
def add1(*args):
    if len(args) > 0:
        sum1 = 0
        for i in args:
            sum1 += i
        return sum1


# 类
class Calculate:
    def test(self):
        print('奥利给...')
