# @staticmethod
# def 方法名():
#      方法体

# 静态方法是类中函数，它不需要实例。可以理解为是独立 单纯的函数
# class Dog(object):
#     @staticmethod
#     def bark():
#         print('汪汪叫')
# dog=Dog()
# dog.bark()


class A:
    age=18
    @staticmethod
    def get_age():
        return A.age
a=A()
print(a.get_age())    # 实例对象可以去访问静态方法
print(A.get_age())    # 类对象可以去访问静态方法


# --------------------------------------------------------
# 实例方法 类方法 静态方法访问的综合举例
class Test(object):
    def instancefun(self):       # 实例方法
        print('这是instancefun')

    @classmethod              # 类方法
    def classfun(cls):
        print('这是classfun')
        print(cls)

    @staticmethod             # 静态方法
    def staticfun():
        print('这是staticfun')

    def function():          # 普通函数，无参数
        print('这是func')

t=Test()   # 实例化对象

# 调用实例方法
# t.instancefun()     #这是instancefun——————实例对象可以访问实例方法
# Test.instancefun()  # 直接这样访问报错
# Test.instancefun(t)   # 把t作为参数传入给self
# Test.instancefun(Test)

# 调用类方法
# t.classfun()        # 这是classfun——————实例对象可以访问类方法
# Test.classfun()     # 这是classfun——————类对象可以访问类方法

# 调用静态方法
t.staticfun()         # 这是staticfun
Test.staticfun()      # 这是staticfun

# 普通函数调用
# t.function()         # 对象不能直接调用函数
Test.function()        # 这是func—————类调用函数


