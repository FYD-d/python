#and  与
# x and y  ：同真为真，一假全假
# 参数从左向右解析，一旦结果可以确定就停止
# 1）当x为真时。要看y，y为真，返回值为真；y为假，返回值为假。此时，整个表达式的值为y
# 1）当x为假时。整个表达式的返回值为假

# x=1
# y=False
# print(x and y)
#
# x=1
# y=3
# print(x and y)
#
# x=False
# y=2
# print(x and y)

# --------------------------------------------
# or  或    一真即真，全假为假
# 1）当x为真时，整个表达式的返回值为真
# 2）当x为假时，如果y为真，整个表达式的返回值为真；如果y为假，整个表达式的返回值为假

# x=10
# y=False
# print(x or y)
#
# x=False
# y=False
# print(x or y)
#
# x=False
# y=5
# print(x or y)
#
# ----------------------------------------------------------------
#not  非
# print(not 0)    #TRUE
# print(not 1)    #FALSE

# -------------------------------------------------------------------
#练习实例
# 1）年龄0-120
# age=100
# if age>=0 and age<=120:
#     print("年龄正确")
# else:
#     print("年龄不正确")

# 2）只要有一门成绩>=60,为合格
# python_score=50
# c_score=50
# if python_score>=60 or c_score>=60:
#     print("合格")
# else:
#     print("不合格")

# 3)判断是否为本公司员工
# is_employer=True  #代表是本公司员工
# if is_employer:
#     print('可以入内')
# else:
#     print('禁止入内')

#----------------------------------------------------------------------
# 三元表达式
# a=1
# b=2
# print(a if a>b else b)  #条件a>b  ,如果成立，输出a；不成立，输出b
# print('a最大') if a>b else print('b最大')


#-------------------------------------------------------------------------
# 综合运用（猜拳）
# 思路
# 1.控制台输入，用到input函数：限制输入函数为整数
# 2.对手是电脑，随机出拳，用到random函数
#            import  random 模块     随机函数： computer=random.randint(1,3)
#                                            拓展：computer=random.choice('剪刀','石头','布')

# 3.决定胜负
# 你胜利的情况：
# 你          电脑
# 剪刀         布
# 石头         剪刀
# 布           石头
#
# 平局的情况：
# 你和电脑出的一样
#
# 其他情况：你输的情况

import  random
ni=int(input("请出拳：剪刀（1），石头（2），布（3）："))
computer=random.randint(1,3)
print(f'电脑的出拳是{computer}')

#你胜利的情况
if ((ni==1) and (computer==3)) or ((ni==2) and (computer==1)) or ((ni==3) and (computer==2)):
    print('赢')
#平局情况
elif ni==computer:
    print('平局')
#输的情况
else:
    print('输')





















