# 1.类的私有属性和私有方法，都不能通过对象直接访问，但是可以在本类内部访问
# 2.类的私有属性和私有方法，不能被子类继承，子类也无法访问
# 3.类的私有属性和私有方法，往往用来处理内部的事情，不通过对象来处理，起到安全作用


# ------------------------------------------------------------------------------
# 定义私有属性和方法
# 各种下划线格式的作用
# _x  也代表私有属性或方法，实际上类对象 和子类可以访问
# __x 私有成员
# __xx__ ：用户名字空间的魔法对象和属性
# xx_  用于避免与python关键词的冲突  class

# class Classmate:
#     name='lucy'
#     _age=20
#     __sex='F'
#
# pr=Classmate()

# # 通过类访问属性
# print(Classmate.name)   #lucy 类内部可以访问这些属性
# print(Classmate._age)   #20
# # 私有属性,外部不能直接访问
# # print(Classmate.__sex)  #'Classmate' object has no attribute '__sex'
#
# # 强行获取私有属性  语法:  对象._类名__属性名
# print(pr._Classmate__sex)

# # 通过对象访问属性
# print(pr.name)   #lucy
# print(pr._age)   #20  _age只是告诉别人是私有属性,但别人可以访问
# print(pr.__sex)  #AttributeError: 'Classmate' object has no attribute '__sex'   外部不能访问


# 通过正规手段访问私有属性
# 1) 在类内部的公有方法中去使用私有属性
# 2) 在外部调用共有方法,以间接地使用私有属性
# class Classmate:
#     def __init__(self):
#         # 定义私有属性__name__
#         self.__name__='哈哈'
#
#     def funa(self):
#         # 在类方法中使用私有属性
#         print(self.__name__)
#
# pr=Classmate()
# # print(pr.__name)   #AttributeError: 'Classmate' object has no attribute '__name'
# pr.funa()


# 私有方法
# 1) 在类中定义一个公有的方法
# 2) 在类中公有的方法中去调用私有的方法
# 3) 外部访问通过调用公有方法,实现对私有方法的访问
# class Classmate:
#     # 定义私有方法 __sing()
#     def __sing(self):
#         print('唱歌')
#     # 定义公有方法
#     def dance(self):
#         print('跳舞')
#         self.__sing()
#
# pr=Classmate()
# # print(pr.__sing())   #AttributeError: 'Classmate' object has no attribute '__sing'
# pr.dance()


# -----------------------------------------------------------------------
# 修改私有属性
# 修改属性的值的两种方法:
# 1) 对象名.属性名=数据    --------直接修改
# 2) 对象名.方法名()     ---------间接修改

class Classmate:
    def __init__(self):
        self.name='lucy'
        self.__age= 18

    #获取私有属性的值
    def get_age(self):
            return self.__age

    def set_age(self,new_age):
        self.__age=new_age

pr=Classmate()

# 强行获取私有属性获取
print(pr._Classmate__age)  #18

# 想在类的外面获取对象的属性
ret=pr.get_age()
print(ret)
pr.get_age()

# 想在类的外面修改对象私有属性的值
pr.set_age(30)
print(pr.get_age())
















