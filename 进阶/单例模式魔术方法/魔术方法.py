# class A:
#     pass
#
# print(dir(A))  # 查看所有属性和方法


# 1.__doc__ 获取到注释内容
# class A:
#     '''表示类的描述信息'''
#     def funa(self):
#         pass
#
# print(A.__doc__)  #打印类的注释信息    表示类的描述信息


# 2.__module__ 表示当前操作的对象在哪个模块(读取使用的模块名)
# __class__ 表示当前操作的对象的类是什么(读取类名)
# from b1 import A
# obj=A()
# print(obj.__module__)  # b1
# print(obj.__class__)   # <class 'b1.A'>

# 3.__call__ 允许实例对象能像函数一样去调用实例方法
# class A:
#     def __init__(self):
#         print('这是init')
#     def __call__(self):
#         print('这是call')
#
# # 法一
# a1=A()     # 创建实例对象         这是init
# a1()       # 自动调用call方法     这是call
#
# # 法二
# A()()


# 4.__dict__ 查看类或对象中的所有属性
# class A:
#     mind='哈哈'
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def func(self):
#         print('func')
#
# # 查看类的属性，即类属性、方法
# print(A.__dict__)
#
# # 获取对象obj的属性
# obj=A('zs','20')
# print(obj.__dict__)

# dir() 与 __dict__ 的区别：
# dir()是函数，返回的是一个列表；__dict__返回的是一个字典；
# dir() 用来寻找一个对象的所有属性，包括__dict__中的属性。   __dict__是 dir()的子集
# __dict__并不是所有对象都拥有的属性，许多内建类型没有__dict__属性，如list


# 5.__str__() 打印实例对象时，返回自定义的字符串————输出是给用户看的
#   __repr__()————输出是给程序员看的
class Human:
    def __repr__(self):
        return 'hello'

h1=Human()
print(h1)   # 如果不用__repr__(),本来打印实例对象的引用


# 6.__getitem__   __setitem__  __delitem__
class Test:
    def __getitem__(self,key):
        print('这是geetitem',key)

    def __setitem__(self,key,value):
        print('这是setitem',key,value)

    def __delitem__(self,key):
        print('这是delitem',key)

te=Test()
# 赋值-获取
res=te['name']   # 自动触发执行 __getitem__()
# 修改
te['name']='zs'  # 自动触发执行 __setitem__()
# 删除
del te['name']   # 自动触发执行 __delitem__()
