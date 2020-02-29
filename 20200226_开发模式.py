# 开发模式：单例模式

class Singleton:
    # 私有化,单例地址存在于__instance
    __instance = None

    # 重写__new__
    def __new__(cls):
        if cls.__instance:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance


s = Singleton()
s1 = Singleton()
print(id(s) == id(s1))  # True
