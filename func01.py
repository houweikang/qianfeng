"""
pycharm快捷键
格式化 Ctrl + shift + F
快速提示 alt + enter
"""

'''
无参数函数：

def func():
    pass

func()  ----> 调用

有参数函数：
    1. 普通参数
    def func(name,age):
        pass

    func('aa',18) ----> 形参与实参个数要一致

    2. 可变参数
        A.def func(*args):
                pass

            func() ----> 实参个数可以无，可以多个  注意：*不能是关键字参数


        B.def func(**kwargs):
            pass

            func() ----> 实参个数可以无，可以多个  注意：**必须是关键字参数


        C.def func(*args,**kwargs):
            pass

            l1 = [1,2]
            d1 = {'1':'a','2':'b'}
            func(*l1,**d1) #func(1,2,'1'='a','2'=b) 拆包

        D.混用

        def func(name,*args,**kwargs):
            pass

        func('tom') ---> 必须赋值name
    3. 默认值+关键字

    def func(name,age=18):
        pass

'''


# 返回值
def add1(a, b):
    result = a + b
    return result, 'a'  # 若返回多值，会全部放入一个元组中，作为整体返回


x, y = add1(1, 2)
print(x, y)
x = add1(1, 2)
print(x)

# 局部变量 函数内部声明的变量
# 全局变量 函数外侧声明的变量，所有函数都可以访问

# global 若需要在函数内部修改全局变量，global 全局变量
# 若全局变量可变，例如[],则不需要加 global


# 内部函数
'''
特点：
1. 可以访问外部函数变量
2. 内部函数可以修改外部函数的可变类型变量，比如：list
3. 内部函数修改全局不可变变量，需声明: global 变量
    修改外部函数的不可变变量，需声明: nonlocal 变量
4. locals() 查看本地变量，以字典形式输出
    globals() 查看全局变量，也是以字典形式输入（注意里面有系统变量存在）
'''

# 闭包
'''
条件：
1. 外部函数在定义了内部函数
2. 外部函数有返回值：内部函数名（无括号）
3. 内部函数引用了外部函数的变量

格式：
def 外部函数():
    ....
    def 内部函数():
        ....
    return 内部函数  #没有括号

a = 外部函数()
# 调用内部函数：
a()

 



    
'''