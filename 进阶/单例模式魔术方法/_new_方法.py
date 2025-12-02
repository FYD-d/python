# __init__() 初始化设置————实例对象创建时会自动调用的方法
# __new__() 是第一个在创建对象时真正被调用的方法
# __new__()的作用： ——————如果不设置，系统选择默认
# 1) 在内存中为对象分配空间
# 2) 返回对象的引用，返回值会引发__init__()调用


# -------------------------------------------------------
# __new__()没有返回值的情况
# class Person:
#     def __new__(cls, *args, **kwargs):    # 创建实例时，第一个调用__new__()
#         print('这是new方法中的cls',cls)
#         print('这是new方法')
#
#     def __init__(self):
#         print('这是init方法')
#
# p=Person()
# print('这是类',Person)

# -------------------------------------------------
# # 重写new方法，提供返回值   引用init的调用
# class Person(object):
#     def __new__(cls, *args, **kwargs):    # 创建实例时，第一个调用__new__()
#         print('这是new方法中的cls',cls)
#         print('这是new方法')
#         # 调用父类__new__()方法，传参cls；——————当前类创建实例对象
#         return object.__new__(cls)  # 法一
#         return super.__new__(cls)   # 法二
#
#     def __init__(self):
#         print('这是init方法')
#
# p=Person()
# print('这是类',Person)

# ---------------------------------------------------
# new 返回对象的引用
class Iphone(object):
    def __new__(cls, *args, **kwargs):
        print('这是new中cls',cls)
        print('创建对象，分配空间')
        ins=super().__new__(cls)       # 通过调用父类__new__()来创建当前类的实例对象

        return ins                # 返回对象的引用

    def __init__(self):
        print('这是init中的self',self)
        print('手机初始化')

print('这是类',Iphone)
pho=Iphone()
print('这是实例化对象',pho)


# --------------------------------------------------------
# __init__()与__new__()的区别：
# 1) __new__()是真正在创建实例对象时被第一个调用的方法，该方法返回对象的引用时,会引发__init__()的调用
# 2) __new__()的第一个参数时cls ，__init__() 的第一个参数是self
# 3) __new__() 必须有返回值，且返回的是对象的引用，否则__init__()不会调用






