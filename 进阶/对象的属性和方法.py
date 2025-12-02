# 对象的属性和方法

# 1.添加和获取对象的属性
# # 定义类（创建类）
# class Hero(object):
#     # 定义一个方法
#     def move(self):
#         print('正在前往事发地点')
# # 创建对象，实例化对象
# hero=Hero()
#
# # 给对象添加属性
# hero.name='lucy'   #添加对象的name属性
# hero.hp=2500     #生命值
# print('英雄%s的生命值：%d'%(hero.name,hero.hp))
# hero.move()  # 调用实例方法
from 基础.字符串.字符串的常用操作详解 import name2


# 2.在方法内通过self获取对象属性
class A():
    def test(self):
        print('%s的年龄是%d'%(self.name,self.age))   # name age 是类中的属性

# a=A()  #实例化一个对象a
# a.name='lucy'
# a.age=22
# a.test()  #调用实例方法     对象.方法
# print(a.__dict__)  #查看对象中的所有属性    {'name': 'lucy', 'age': 22}
#
# a.job='IT'
# print(a.job)


# ---------------------------------------------------------------------
# 实类属性与类属性的区别以及使用方法
# 类属性：属于类      实例属性：属于对象

# 创建类
class B:
    num=0      #类属性
    def __init__ (self,name):
        self.name = name #实例属性，在__init__内部定义
    def test(self):
        print(f'我的名字是{self.name}')

# 实例对象
b=B('zs')
# print(b.name)   # zs  对象可以访问实例属性
# print(B.name)   # AttributeError: type object 'B' has no attribute 'name'   类不能访问实例属性

# print(b.num)   # 0 对象可以访问类属性
# print(B.num)   # 0 类可以访问类属性

b.test()   # 我的名字是zs
























