#可迭代对象：能通过for循环一个个把数取出来的对象
#range()函数：
# range(start,end,step):
# range(1,10,2)  范围左闭右开[1，5)  步长为2
# from symbol import continue_stmt

# for i in range(5)  #默认从0开始，步长为1 [0,5)
#     print(i)


#计算1-100求和
sum=0
for i in range(1,101):
    sum=sum+i
print(sum)

# 九九乘法表

# for row in range (1,10):  #行数范围1-9
#     for col in range(1,row+1):  #列数范围 1-row
#         print(f'{col}*{row}={col*row}',end=' ')
#     print()


# ------------------------------------------------------------------
# break 和continue只能够在循环体内使用
# break：退出所在循环的当前循环，不再继续当层循环
# a=0
# while a<3:
#     a+=1
#     print(a)
#     break


# continue:结束当前循环的本轮循环（continue后面的代码不在执行），继续下一轮
# a=0
# while a<5:
#     a=a+1
#     if a==3:
#         continue  #此时后面代码不执行，继续下一轮
#     print(a)











































