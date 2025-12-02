# 一.匿名函数
# 匿名函数：对简单函数的定义
# 形参的数量按需加，加多少都可以，只要用逗号隔开就可以
# 格式：  函数名=lambda  形参：返回值
# # 求和函数
# def func(a,b):
#     return a+b
# print(func(1,2))   # 3
#
# # 匿名函数
# func=lambda a,b:a+b
# print(func(1,2))   # 3
from pandas.core.construction import sanitize_array

# # 在字符串中，返回索引中为0和2对应的元素
# str1='abcd'
# # 法一
# a=[]
# a.append(str1[0])
# a.append(str1[1])
#
# # 法二
# li=list(str1[0:3])
# li.remove('b')
# print(li)

# # 法三
# func=lambda x:[x[0],x[2]]
# print(func('abcd'))

# -----------------------------------------------------------------------
# a=3
# b=4
# print(a) if a>b else print(b)
# # 三目运算语法: 表达式1或结果1  if 条件  else  表达式2或结果2

# #匿名函数实现上例
# func=lambda a,b:a if a>b else b
# print(func(3,4))

# -------------------------------------------------------------------------
# # 求平方
# a=lambda x:x**2
# print(a(3))

# --------------------------------------------------------------------------
# 二.内置函数
# 查找内置函数
# import builtins
# print(dir(builtins))

# # list()
# a='abc'
# print(a)         #abc
# print(list(a))  #将a转换为列表形式      ['a', 'b', 'c']
#
# # abs() 返回绝对值
# print(abs(-3))   # 3

# sum([]) 求和
print(sum([1,2,3]))

# min([]) 求最小值    max([]) 求最大值
print(min([1,2,3]))

# ---------------------------------------------------------
# # zip() 拉链函数 ：将对象中对应的元素打包成一个个元组的形式，然后返回由这些元组组成的内容
# a=[1,2,3]
# b=['a','b','c']
# print(zip(a,b))   #<zip object at 0x000001D4999905C0>
# print(list(zip(a,b)))   #[(1, 'a'), (2, 'b'), (3, 'c')]

# # 每个变量元素个数不一致时
# a=[1,2,3]
# b=['a','b','c','d']
# c=(6,5,4,3,2,1)
# for i in zip(a,b,c):
#     print(i)

# map()函数
# map(function,iterable)  映射函数
# 作用：可对可迭代对象中的每一个元素进行映射，分别执行function
# # 计算列表中每个元素的平方，返回新列表
# li=[1,2,3,4]
# def fun(x):
#     return x**2
# mp=map(fun,li)
# print(list(mp))    #[1, 4, 9, 16]
#
# # 使用匿名函数
# print(list(map(lambda x:x**2,li)))  #[1, 4, 9, 16]
#
# fun=lambda x:x**2
# print(list(map(fun,li)))  #[1, 4, 9, 16]

# reduce() 减少 降低  可迭代中通过计算使元素不断减少，最终得到一个计算值
# 语法： reduce(函数名，可迭代对象)
# from functools import reduce   # 导入模块
# def func (x,y):
#     return x+y
#
# result=reduce(func,[1,2,3,4])   #求累计和
# print(result)
#
# # 用匿名函数
# i=reduce(lambda x,y:x+y,[1,2,3,4])
# print(i)

# enumerate枚举  用于将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标，一般用在for循环
# 语法:enumerate(可迭代对象，[start=0])
li=['a','b','c']
for i,j  in enumerate(li):
    print(i,j)
print(list(enumerate(li)))   #[(0, 'a'), (1, 'b'), (2, 'c')]
print(dict(enumerate(li)))   #{0: 'a', 1: 'b', 2: 'c'}

# ----------------------------------------------------------------------------------
# 三.拆包
# def test():
#     a=10
#     b=20
#     c=30
#     return a,b,c
# print(test())   #return 返回多个值，以元组形式返回到函数的调用出   (10, 20, 30)
#
# a1,b1,c1=test()    #以元组的形式返回到函数的调用出    a1,b1,c1=(10, 20, 30)   拆包的过程
# print(a1)   #10
# print(b1)   #20
# print(c1)   #30
# print(a1,b1,c1)     #10 20 30


# 元组拆包进阶
# tu=(1,2,3,4)
# a,*c,b=tu
# print(f'a={a}')  #a=1
# print(f'c={c}')  #c=[2, 3]
# print(f'b={b}')  #b=4
#
# # 列表拆包
# a,*b=1,2,3
# print(a)   #1
# print(b)   #[2, 3]

# 字典拆包
dic={'name':'fyd','age':18,'gender':'male'}
a,b,c=dic
print(a,b,c)   #name age gender
# 注意：对字典 拆包后获取的是字典的key，没有value













