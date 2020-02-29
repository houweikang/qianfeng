'''
面向对象：
程序        现实
对象 ----》具体的事物

现实中的事物---》转成电脑程序
世间万物皆对象

类：
对象
属性
方法
'''

# 类名首字母大写，多单词驼峰式命名

'''
class 类名([父类]):
    属性：特征
    
    方法：动作
    
类属性
对象属性

类中方法：动作
种类：普通方法 类方法 静态方法 魔术方法
普通方法格式：
    def 方法名(self[,参数,参数]):
        pass
类方法：
    @classmethod
    def 方法名（cls[,参数]）:
        pass
        
    类名.方法名()
    对象.方法名()

静态方法：
    @staticmethod
    def 方法名([参数]):
        pass

    类名.方法名()
    对象.方法名()    
    
魔术方法：
    重点：
        __init__：初始化，创建完空间后调用的第一个方法
        __str__:单纯打印对象名称，出来是一个地址。若有__str__ 会返回return 下的信息
    了解：
         __new__:实例化
         __call__:对象调用方法，当将对象当函数使用时，默认调用此函数
         __del__:
            1.对象赋值
                p = Person()
                p1 = p
                p 、p1 共同指向同一个地址
            
            2.删除地址的引用
                del p1 删除p1对地址的引用
                
            3.查看对地址的引用次数
                import sys
                
                print(sys.getrefcount(p)- 1) 
            
            4.当一块内存没有了任何引用，默认执行__del__
'''


class Phone:
    # 类属性
    brand = 'HW'
    price = 4999
    type = 'mate 80'

    # 魔术方法之一
    def __init__(self):  # 初始化
        self.brand = 'xiaomi'

    # 普通方法
    def call(self):
        print('正在打电话....')


# 私有化
# 封装：1.私有化属性 2.定义共有set和get
# __属性：属性私有化，访问范围仅限于类中
'''
好处：
1.隐藏属性不被外界随意修改(外界还是能够访问，对象._类名__属性)
2.通过函数修改
    def setXXX(self,XXX):
    3.可以在函数中限制属性赋值
        if ....:
            self.__XXX = XXX
4.可以通过get获取具体某一个属性
    def getXXX(self):
        retrun self.__XXX
'''


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = 59

    # 定义共有set和get
    # set是为了赋值
    def setScore(self, score):
        self.__score = score

    # get是为了取值
    def getScore(self):
        return self.__score

    def __str__(self):
        return '姓名：{},年龄：{},分数：{}'.format(self.name, self.age, self.__score)


yp = Student('yupeng', 18)
print(yp)


# 在开发中看到一些私有化处理:装饰器
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = 59

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score


# 继承：is a ,has a
'''
继承：
    Student,Employee,Doctor  ---> 都属于人
    相同代码  冗余，可读性差
    
    将相同代码提取到 ---》 Person类
        Student,Employee,Doctor 继承Person
        
        class Student(Person):
            pass
            
    特点：
        1.若类中不定义__inti__,调用父类中的__init__；
        2.要定义自己的__init__,再调用父类的__init__,使用super().__init__()
        3.使用方法，默认先找当前类，再找父类
            重写，在子类中重写方法 
            
    python允许多继承
        def 子类(父类1,父类2):
            pass
        
        若父类中含有相同的方法
        广度优先   .__mro__ ---》查看顺序       
'''

class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):

        msg = '{}品牌的车在{}上以{}速度行驶'.format(self.brand, road.name, self.speed)
        print(msg)

    def __str__(self):
        return '{}品牌，速度：{}'.format(self.brand, self.speed)


# 创建实例化对象
r = Road('京藏', 12000)
audi = Car('奥迪', 120)
audi.get_time(r)

#多态
