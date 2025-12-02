# class Tool(object):
#     self.age=20        # 属性
#     def funa(self):    # 实例方法
#         print(123)
#
# t=Tool()



# 类方法————针对类对象定义的方法
# 在类方法内部可以直接访问类属性 或调用类方法
# class 类名:
#       @classmethod     ——————类方法的标志
#       def 方法名(cls):  ——————第一个参数必须是cls（代表的是当前类名）
#           方法体

# 类方法内部使用类属性： cls.属性
# 类方法内部使用类方法： cls.类方法()
# 类方法本质：将类本身作为对象进行操作的方法


# -----------------------------------------------------
# class Person:
#     age=20
#     # 类方法
#     @classmethod
#     def human(cls):      #类属性
#         return cls.age  # 类名，属性来操作
#
# # 实例化对象p
# p=Person()
# print(p.human())    # 实例对象可以访问类对象
# print(Person.human())  # 可以通过类对象引用，即类本身调用类的方法

# ------------------------------------------------------------
class Person:
    age=20
    @classmethod
    def get_age(cls):    # 获取类属性
        print(cls.age)

    @classmethod
    def set_age(cls,age):
        cls.age = age

p=Person()
p.get_age()           # 实例对象.类方法 来获取属性
Person.get_age()      # 类对象。类方法 来获取属性

p.set_age(18)
p.get_age()           
Person.get_age()      # 18









