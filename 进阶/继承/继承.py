# 继承的特点：
# 继承可以使得子类具有父类的各种属性和方法，而不需要再次编写相同的方法
from symbol import pass_stmt

# 如果一个类A的属性和方法可复用，则可通过继承传递给类B
# 此时A为父类，B为子类

# 继承的优点：
# 1.减少了重复的代码
# 2.增加了类的耦合性 （模块间的关联程度）
# 3.使得代码更加的规范化，合理化

# 继承格式
# class 类名 (父类名):
#     pass    # 什么执行语句都没有时，可写pass

# # 例1.不使用继承
# class Person:
#     def sing(self):
#         print('唱歌')
#     def dance(self):
#         print('跳')
#
# p=Person()
# p.sing()
# p.dance()

# # 例2  使用继承
# class God:
#     def sing(self):
#         print('唱歌')
#     def dance(self):
#         print('跳')
#
# class Person(God): #Person类继承父类God
#         pass
#
# # 创建对象
# p=Person()
# p.sing()

# ----------------------------------------------
# 新式类与旧式类
# python3 中类的定义
# 1.法一
# class Person(object):
#     pass

# 2.法二
# class Person():
#     pass

#3.法三
# class Person():
#       pass


# ------------------------------------------------------
# 单继承
# class Person():
#     Sname='动物类'
#     def __init__(self,name,sex,age):
#         self.name=name
#         self.sex=sex
#         self.age=age
#
#     def eat(self):
#         print(f'{self.name}在吃东西，性别是{self.sex},年龄是{self.age}')
#
# # 定义子类
# class Lucy(Person):
#     pass
#
# p1=Lucy('Lucy','女',18)
# p1.eat()


# 继承的传递性
# 爷爷类
class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print('吃')
    def print(self):
        print('睡')

# 爸爸类
class Dog(Animal):
    def bark(self):
        print(f'{self.name}在叫')

# 儿子类
class Black(Dog):
    def fly(self):
        print(f'{self.name}会飞')

dog=Dog('狗')
dog.bark()

# black=Black('小黑')
# black.fly()













