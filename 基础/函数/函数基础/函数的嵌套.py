# 1.在一个函数内部调用另一个函数
# def funa():
#     print('这是funa')
#
# def funb():
#     print('这是funb')
#     funa()      #在一个函数funb()内部调用另一个函数funa()
# funb()       #只要调用funb()即可


# 2.嵌套  在一个函数中定义另一个函数
# def funa():
#     def funb():
#         print('这是funb')
#     print('这是funa')
#     funb()
# funa()


# 定义多行的函数
# def funa():
#     print('——'*50)     # 定义一行的函数
# def funb(num):
#     i=0
#     while i<num:
#         funa()
#         i+=1
# funb(3)


# 骰子  特点：1-6个面
import random
def play(n):
    sum=0
    for i in range(n):
        sum+=random.randint(1,6)   #从1-6中随机取数
        print(f'值={sum}')
    return sum

result=play(3)
print(result)

