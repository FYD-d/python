# 单例：是一个特殊的类，这个类只能够创建一次实例对象
# 单利模式：让所有类在实例化时，指向同一个内存地址。

# 为什么要有单例模式：
# 节省内存空间，因为产生不同的对象，会产生不同的内存地址，造成资源的浪费


# -------------------------------------------------------------
# 设置单例模式的本质：
# 1.判断这个实例是否存在
# 2.如果存在，则返回这个实例；如果不存在，则创建这个实例对象


# 1) __new__()实现单例模式——————指向同一个内存地址
# class Person:
#     pass
# a=Person()
# b=Person()
# print(id(a))    #1920079584272
# print(id(b))    #1920079584272


# class Test(object):
#     ins=None             # 属性——————用来保存实例对象的引用(类似变量赋值）
#     def __new__(cls, *args, **kwargs):
#         if cls.ins is None:
#             cls.ins=super().__new__(cls)    # 创建实例对象
#             # cls.ins=object.__new__(cls)    #法二
#
#         return cls.ins
#
# t1=Test()
# t2=Test()
# print(t1)    #<__main__.Test object at 0x0000024D806913D0>
# print(t2)    #<__main__.Test object at 0x0000024D806913D0>

# 思路：
# 1.定义一个类属性，初始值是None，用于记录单例对象的引用
# 2.重写__new__()方法
# 3.如果类属性是None，调用父类分配空间，并在类属性中记录结果
# 4.返回类属性中记录的对象引用


# 2) 通过 @classmethod 实现
# class Sing(object):
#     instance=None
#     @classmethod
#     def get_instance(cls):
#         if Sing.instance is None:
#             Sing.instance=super().__new__(cls)
#
#         return Sing.instance
#
# a=Sing.get_instance()
# b=Sing.get_instance()
# print(id(a))      #2107501515344
# print(id(b))      #2107501515344


# 3) 通过装饰器实现
# @语法糖,装饰器函数本质是闭包函数
# def outer(fn):   #类名作为参数传递给fn
#     _ins={}
#     def inner():
#         if fn not in _ins:
#             _ins[fn]=fn()      # key=value 把fn() 值传入到字典
#             print(fn)
#             print(_ins)
#             print(_ins[fn])
#         return _ins[fn]
#     return inner
#
# @outer
# class A(object):
#     a=1
#
# a1=A()
# a2=A()
# print(id(a1))
# print(id(a2))


# 4) 通过导入模块时实现
# from test import Test
# from test import Test

# python 的模块是天然的单例模式，因为模块第一次导入时会加载到内存空间。第二次及以后再导入时，只会引用不会再次执行模块代码


# 4) 通过元类实现
# hasattr()函数 用于判断函数对象是否包含对应的属性
# 参数是一个对象和一个字符串，如果字符串是对象的属性值，函数则返回True，否则返回False
# class A:
#     b=2
#     def test(self):
#         print('这是test')
#
# # 判断是否包含属性
# print(hasattr(A(),'b'))      #True
# # 判断是否包含test方法
# print(hasattr(A(),'test'))   #True


# 使用hasattr() 来实现单例模式
class A:
    def __init__(self,name):
        self.name=name    # 实例属性

    def __new__(cls, *args, **kwargs):
        # ins 不存在时执行if内的代码
        if not hasattr(cls, 'ins'):    #hasattr(cls,'ins')为False，代表ins不存在
            cls.ins=super().__new__(cls)

        return cls.ins

a=A('张三')
b=A('李四')
print(id(a))
print(id(b))
print(a.name)
print(b.name)




























