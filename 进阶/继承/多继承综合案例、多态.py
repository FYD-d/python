# # 机器人一代
# class Robot(object):
#     def __init__(self,year,name):   # 初始化设置
#         self.year=year              # 实例属性
#         self.name=name
#
#     def walk(self):
#         print('%s 只能平地行走，遇到障碍物会摔倒'%self.name)
#
#     def produce(self):
#         print('{}年生产的机器人，名字是{}'.format(self.year,self.name))
#
# rot=Robot(2000,'罗马一代')
# rot.walk()
# rot.produce()
#
# # 机器人二代
# class Robot2(Robot):
#     def walk(self):
#         print('%s可以避开障碍物'%self.name)
#
# rot2=Robot2(2002,'罗马二代')
# rot2.walk()
# rot2.produce()
#
# # 机器人三代
# class Robot3(Robot2):
#     def run(self):
#         print('%s可以跑步'%self.name)
#
# rot3=Robot3(2004,'罗马三代')
# rot3.run()
# rot3.produce()


# -------------------------------------------------------
# 多态：同一种事物的多种形态
# 多态性：一真调用方式，不同的执行效果

# 多态性的好处
# 1）可以增加代码的灵活性
# 2）以继承和重写父类方法为前提
# 3）是调用方法的技巧，不会影响到类的内部设计

# 容器类型有多种形态：字符串、列表、元组、字典......
# 动物有多种形态：人、狗、猫......

# ------------------------------------------------------
# # 1.+号的多态性
# print(1+2)                  # + 在此处代表运算
# print('hello'+'phthon')     # + 在此处代表字符串的拼接

# # 2.len() 传不同的参数，也体现多态
# print('world',len('world'))
# print([1,2,3],len([1,2,3]))

# 3.动物的多态性
# class Animal:
#     def run(self):
#         print('动物在走')
#
# class People(Animal):
#     def run(self):
#         print('人在走')
#
# class Dog(Animal):
#     def run(self):
#         print('狗在走')
#
# people=People()
# dog=Dog()
# # 多态的意义是根据不同的对象做不同的事情
# people.run()
# dog.run()

# ----------------------------------------------------------
# 要实现多态的两个前提#：
# 1.继承：多态必须发生在父类与子类之间
# 2.重写：子类重写父类方法

class A:                # 父类
    def show(self):
        print('A.show')

class S1(A):            # 子类S1
    def show(self):
        print('S1.show')

class S2(A):           # 子类S2
    def show(self):
        print('S2.show')

# 定义一个统一接口
def func(obj):
    obj.show()    # 调用show()方法

s1=S1()
func(s1)         #S1.show

s2=S2()
func(s2)         #S1.show

# 现在想增加S3类
class S3(A):           # 子类S3
    def show(self):
        print('S3.show')

s3=S3()
func(s3)         #S3.show



















