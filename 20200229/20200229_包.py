# 文件夹：非py文件
# 包：py
# 一个包中可以存放多个模块
# 项目 》 包 》 模块 》类 函数 变量

# 使用包中模块中的article类
'''
__init__.py文件
导入包的时候，自动调用__init__.py文件
作用：
1.初始化其中的函数、变量、类
2.可以通过 包.函数 访问
3.结合 __all__=[定义通过 from 包 import * 调用的模块]
'''

from article.models import Article, Tag

a = Article('haha')
a.show()
t = Tag('a')
t.show()

'''

from 包 import *  表示该包中内容（模块）是不能访问，需要在__init__.py
    文件中定义 __all__ = [] 访问的内容

'''
