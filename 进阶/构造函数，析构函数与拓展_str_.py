# 创建对象的时候就已经拥有的属性
# __init__具有初始化作用，当该类被实例化时会自动执行该函数。那么通常可把要初始化的属性放在这个方法里去
from tkinter.font import names


# 注意
# 类里面没有写__init__(),python会自动创建，但是不执行任何操作
# class Hero:
#     def __init__(self):   #初始化
#         self.name='泰坦'
#         self.hp=200   #生命值
#         self.at=450   #攻击力
#     def move(self):
#         print(f'{self.name}正在移动')
#     def attack(self):
#         print(f'{self.name}的生命值{self.hp},攻击{self.at}')
# 创建对象
# hero=Hero()   #调用方法
# hero.move()
# hero.attack()


# 实例每个对象，让每个对象拥有不同属性值
# class Hero:
#     def __init__(self,name,hp,at):   #初始化
#         self.name=name
#         self.hp=hp  #生命值
#         self.at=at   #攻击力
#     def move(self):
#         print(f'{self.name}正在移动')
#     def attack(self):
#         print(f'{self.name}的生命值{self.hp},攻击{self.at}')
# # 创建对象
# hero1=Hero('大乔',400,300)   #调用方法
# hero2=Hero('小乔',300,200)
# hero1.move()
# hero1.attack()
# hero2.move()
# hero2.attack()

# __init__() 构造函数  创建对象———通常用来做属性初始化或赋值操作  python解释器默认调用


# ------------------------------------------------------------------
# __del__() 析构函数   删出对象，python解释器默认调用
# 析构函数用于在对象清除后清除他所占的内存空间

# 作用：主要用于对那些长期占用内存的临时变量进行销毁

# 注意事项：
# 1.构造函数和析构函数一样，不能有返回值
# 2.构造函数不能有参数
# 3.一个类只有一个析构函数
# 析构函数在对象销毁时被调用

# 当对象在某个作用域中调用完毕，在跳出其作用域时，析构函数会被调用一次，可以用来释放内存空间
# class Person:
#     def __init__(self):      # 构造函数
#         print('我是init方法')  #析构函数
#     def __del__(self):
#         print('被销毁')
#
# # 创建对象
# st=Person()
# print('最后一句')
# print('最后一句')
# def funa():
#     print(123)
# funa()


# class Person:
#     def __init__(self):      # 构造函数
#         print('我是init方法')
#     def __del__(self):   #析构函数
#         print('被销毁')
#
# xm=Person()
# del xm     #手动删除对象
# print('最后一句')

# -------------------------------------------------------------------------
# __str__() 函数 ————能够在输出对象变量时，打印自定义的内容
# 注意：
# 1.__str__() 必须返回一个字符串
# 2.定义了__str__()方法，在打印对象，默认输出该方法的返回值

# 例1
# class A:
#     def __str__(self):
#         return 'hello'
# obj=A()
# print(obj)    #hello

# 例2
class Human:
    mind='哈哈'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def work(self):
        print(f'你的名字{self.name}')

    def __str__(self):
        return '你的名字是%s，你的年龄是%d'%(self.name,self.age)

obj=Human('fyd',18)
print(obj)




















