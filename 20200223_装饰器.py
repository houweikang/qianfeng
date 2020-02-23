# 装饰器


# 带参数的装饰器

def outer(n):  # 第一层 接收装饰器参数
    def decorator(func):  # 第二层 接收函数
        def wrapper(*args, **kwargs):  # 第三层 接受函数参数
            func(*args, **kwargs)
            print('-----铺地板{}块'.format(n))

        return wrapper

    return decorator


@outer(10)
def house(time):
    print('{}这天我们拿到了毛坯房...'.format(time))


house('2020-02-23')


@outer(100)
def street():
    print('新修路...')


street()
