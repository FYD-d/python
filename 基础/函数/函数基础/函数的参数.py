# def add():
#     a=1
#     b=2
#     return a+b
# print(add())    #调用上面的函数

# -------------------------------------------------------
# 优化
# 函数的参数：本质是将函数的实际参数传给形式参数的过程
# def add(a,b):   #a，b是形式参数
#     print(a+b)
# add(1,2)    #传递实际参数

# 意义：通用性更加强，可以认为是一个模板

# ---------------------------------------------------------
# 1.必选参数 ：定义了几个，就必须传几个
# def funb(a,b):
#     result=a-b
#     print(result)
# funb(1,2)    #-1
# funb(3)       #TypeError: funb() missing 1 required positional argument: 'b'

# 2.默认参数 ：定义时设置，格式是 形式参数=默认值
# 不传参时，使用定义时的默认值
# 如果传参，则使用传参值来更新数据   (有则更新，无则默认)
# def funa(a=12):
#     print(f'a={a}')
# funa()   #a=12
# funa(3)  #a=3

# 3.可变参数 ：接收多个值时，以元组形式接收
# 传o-任意多个值
def funb(*b):   #真正起作用的是*， b可以取其他名
    print(b)
    print(type(b))  #<class 'tuple'>
funb(1,2,3)     #(1, 2, 3)    元组形式

# #4.关键字参数  传参格式 ：形式参数名 key=value(实参)
# def funb(**key):  #关键字传参   key关键字变量名
#     print(key)
# funb(name='fyd',age=18)  #在实参处以key=value这样的形式（字典形式）来传参

# -------------------------------------------------------------------------------------------
# 拓展：命名关键字参数
# 应用场景：要限制关键字参数的名字的时候
# 特殊点：需要更新数据，则传参时需要以key=value形式传参
# def person(name,age,*,city='hongkong',job='coder'):
#     print(name,age,city,job)
#
# person('fyd',18,city='shanghai',job='eater')   # fyd 18 shanghai eater
# person('fyd',18,city='shanghai','eater')    #SyntaxError: positional argument follows keyword argument


# -------------------------------------------------------------------------
# 拓展：混合参数
# 参数定义顺序：必选参数（位置参数）  ，默认参数   ，可变参数   ，命名关键字和关键字参数
def fun(a,b=10,*c):
    print(f'a={a}')    #a=1
    print(f'b={b}')    #b=2
    print(f'c={c}')    #c=(3, 4)
    return
fun(1,2,3,4)

def fun(a,b=10,*c,d=55):
    print(f'a={a}')    #a=1
    print(f'b={b}')    #b=2
    print(f'c={c}')    #c=(3, 4, 5)
    print(f'd={d}')    #d=55
    return
fun(1,2,3,4,5)        #d=55 无传参则选默认值












