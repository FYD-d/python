# 无参数的函数（被装饰的函数（业务函数））无参数
# 装饰器函数的本质

# 装饰函数
# def test(fn):    #fn 形参代表真正业务函数的函数名
#     def inner():
#         print('这是inner')
#         fn()
#     return inner
#
# # 法一：
# def t1():
#     print('哈哈')
#
# a=test(t1)   #t1作为参数传入到装饰器函数里面去
# a()

# #法二：
# def test(fn):    #fn 形参代表真正业务函数的函数名
#     def inner():
#         print('这是inner')
#         fn()
#     return inner
# @test
# def t1():
#     print('哈哈')
# t1()

# -----------------------------------------------------------
# 被装饰的函数有参数
# def exam(fn):
#     def inner(a,b):
#         print('inner函数中的值:%s,%s'%(a,b))
#         fn(a,b)
#     return inner
# @exam
# def test(a,b):
#     print('结果是：',(a+b))
# test(1,2)

# # 多层嵌套
# def exam(fn):
#     def funa(x,y):
#         print('hello',x,y)
#         def inner(a,b):
#             print('inner函数中的值:%s,%s'%(a,b))
#             fn(a,b)
#         return inner
#     return funa
# @exam
# def test(a,b):
#     print('结果是：',(a+b))
# test(1,2)(3,4)

# ----------------------------------------------------------------
# 被装饰的函数有不定长参数
# 函数参数定义顺序：
# 必选参数 默认参数 可变参数 命名关键字参数 关键字参数
# def funa(fn):
#     def inner(*args,**kwargs):
#         print('开始计算：{}函数',fn.__name__)
#         fn(*args,**kwargs)
#         print('执行完成')
#     return inner
# @funa
# def add(*a,**b):
#     print(a)
#     print(b)
#
# add(2,3,4,5,6,a=1,b=2)   #关键字传参方式  key=value


# -------------------------------------------------------------
# 回调函数
def test(m,n):
    if m==2:
        n()
    else:
        print('不可调用')
def one():
    print('函数一')
def two():
    print('函数二')

test(2,one)














