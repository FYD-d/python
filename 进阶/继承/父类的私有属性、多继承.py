# 一.父类私有属性和方法
# 不对外公开的，外界及子类都不能直接访问
# 私有属性、方法通常用于做一些内部的事情

# 1.子类对象不能再自己的方法内部，直接去访问父类的私有属性或私有方法
# class A:
#     def __init__(self):
#         self.num1=100
#         self.__num2=200   # __num2私有属性
#     def __test(self):
#         print(f'私有方法{self.num1},{self.__num2}')
#
# class B(A):     #B类继承A类
#     def demo(self):
#         print('哈哈')
#
#         # # 1.在子类的对象方法中，不能访问父类的私有属性
#         # print(f'访问父类的四月属性{self.__num2}')
#         # # 2.在子类的对象方法中，不能调用父类的私有方法
#         # self.__test()
# # 创建一个子类对象
# b=B()
# b.demo()
# # b.__test()      #AttributeError: 'B' object has no attribute '__test'       3.子类不能继承父类的私有方法
# # print(b.__num2)   #AttributeError: 'B' object has no attribute '__num2'     4.子类不能直接访问父类的属性

# ---------------------------------------------------------------------------
# 二.子类对象可以通过父类的共有方法间接访问到私有属性或私有方法
# class A:
#     def __init__(self):
#         self.num1=100
#         self.__num2=200
#     def __test(self):
#         print(f'私有方法{self.num1},{self.__num2}')
#
#     # 定义一个公有方法，来使用私有属性和调用私有方法
#     def test(self):
#         print(f'父类的公有方法{self.__num2}')
#         self.__test()
#
# class B(A):     #B类继承A类
#     def demo(self):
#         print('123')
#         self.test()   # 在子类中调用
#
# b=B()
# # 在外界访问父类的共有属性 / 调用公有方法
# print(b.num1)
# # b.test()   # 在外部调用
# b.demo()


# --------------------------------------------------------------
# 三.多继承：子类可以拥有多个父类，并且具有所有的父类的属性和方法
# class A:
#     def test(self):
#         print('这是test方法')
#
# class B:
#     def demo(self):
#         print('这是demo方法')
#
# class C(A,B):  # C继承A 和 B   子类名（父类名1，父类名2）
#     pass
#
# # 创建一个子类对象
# c=C()
# c.test()
# c.demo()

# ----------------------------------------------------------------------
# 如果不同的父类中存在同名的方法，子类对象在调用方法时，会调用哪一个类中的方法呢？
# class A:
#     def play(self):
#         print('这是儿子')
#
# class B:
#     def play(self):
#         print('这是女儿')
#
# class C(A,B):   # 谁先继承就用谁，执行顺序（就近原则）
#     pass
#
# c=C()
# c.play()
# # 查看C类调用方法的顺序  类名.__mro__
# print(C.__mro__)

# ------------------------------------------------------------------
# 如果多个父类中有同名的属性和方法时，
class A :
    def play(self):
        print('这是儿子')

class B :
    def play(self):
        print('这是女儿')

class C(B,A):   # 谁先继承就用谁   
    def play(self):
        A.play(self)     # 对父类扩展一  调用A类的play()方法
        # super().play()   # 对父类的扩展二    此处有A 和B 两个父类
        print('就是这样')

c=C()
c.play()




















