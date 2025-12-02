# 应用场景：
# 当父类的方法不能满足子类需求时，可以对方法进行重写

# 覆盖父类的方法：在子类中定义一个和父类同名的方法来实现

# 覆盖写——重写
# class Human(object):
#     def __init__(self,name):
#         self.name=name
#
#     def eat(self):
#         print(f'{self.name}在吃饭')
#
# class zs(Human):       # 继承
#     def eat(self):     #重写——在子类中定义一个与父类[同名]的方法来实现
#         print(f'{self.name}在慢慢地吃饭')


# ---------------------------------------------------------------------------
# 对父类方法进行扩展：在子类中重写父类方法 ----本质就是通过手段来调用父类的方法 (在重写方法的内部)

# 扩展父类的方法 (在子类中对父类进行扩展)
# 1.父类名.方法(self)
# class Animal(object):
#     def eat(self):
#         print('吃东西')
#
# class Dog(Animal):
#         def eat(self):
#             Animal.eat()    # 本质上是用父类名调用方法
#             print('啃骨头')
#
# black=Dog()
# black.eat()


# 2.super().父类方法
# # 父类
# class Animal(object):
#     def __init__(self,name):
#         self.name=name
#     def bark(self):
#         print(f'{self.name}在叫')
#         print('哈哈')
# # 子类
# class Dog(Animal):       # 继承
#     def bark(self):      # 对父类进行重写
#         super().bark()   # 表示调用父类的bark()方法
#         print(f'{self.name}在汪汪叫')
#
# white=Dog('小白')
# white.bark()


# ----------------------------------------------------------
# 继承父类构造方法,并进行改写
# 父类
class A :
    def __init__(self,name):
        self.name=name
        print('父类中的名字是:',self.name)

    def test(self):
        print(f'父类中的{self.name}在哈哈笑')

# 子类
class A2(A):
    def __init__(self,name):
        super().__init__(name)    # 调用父类的__init__()方法,在子类__init__()中对父类进行了扩展  (保留父类相关内容)
        # A.__init__(self,name)    # 或使用这种方式扩展
        print(f'子类中的名字是{self.name}')

    def test(self):         # 对父类进行重写 ()
        print(f'子类中的{self.name}在嘻嘻嘻笑')

# 创建子类对象,同时会自动调用__init__()方法
b=A2('july')
b.test()



















