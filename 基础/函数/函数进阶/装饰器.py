# 装饰器的使用方法：
# 1.先定义一个装饰器函数（帽子）（也只可以用类 偏函数实现）
# 2.再定义你的业务函数 或者类（人）-------这是真正要执行的
# 3.最后把这顶帽子带在这个人头上去

# 装饰器的模板
# def wrapper(func):
#     def inner(*args, **kwargs):
#         res=func(*args, **kwargs)
#         return res
#     return inner

# 日志打印器
# 装饰器（本质是闭包函数）
# def logger(func):
#     def wrapper(*args):
#         print('开始计算：{}函数:'.format(func.__name__))
#         # 正在执行的业务函数
#         func(*args)
#         print('计算完')
#     return wrapper

# # 第一种方法
# # 定义的真正的业务函数
# def add(x,y):
#     print('{}+{}={}'.format(x,y,x+y))
#
# # 使用装饰器来装饰函数
# # 把函数名add作为参数传入到装饰函数-------装饰功能的本质
# te=logger(add)
# te(200,30)

# --------------------------------------------------------------
# 第二种方法
# def logger(func):
#     def wrapper(*args):
#         print('开始计算：{}函数:'.format(func.__name__))
#         # 正在执行的业务函数
#         func(*args)
#         print('计算完')
#     return wrapper
#
# @logger
# def add(x,y):
#     print('{}+{}={}'.format(x,y,x+y))
#
# add(1,2)

# -----------------------------------------------------------------
# 拓展：为什么不直接使用函数的封装，给他添加额外功能，而要使用装饰器
# 因为装饰器可以实现代码的复用，一个模板可以给多个业务函数添加额外的功能