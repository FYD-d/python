# a=123
# print(type(str(a)))   #把a转换为字符串
#
# b='123'
# b2=int(b)
# print(type(b2))  #把b转换为整型
#
# c=123
# c2=float(c)
# print(type(c2))   #把c转换为浮点型


# input()输入函数  print()输出函数
# 特点:
#    1.执行到input，等待用户输入，输入完成后才会继续向下执行
#    2.input接受用户输入后，存储到变量
#    3.input会把接收到的任意用户输入的数据都当做字符串处理

# name=input('请输你的姓名：')
# print(name)

# age=input('请输入你的年龄：')
# print('你的年龄是',age)

# a=int(input('请输入一个整数：'))  #限制用户输入整数
# print(a)

b=float(input('请输入一个小数：'))  #限制用户输入浮点数
print(b)