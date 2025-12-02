# return返回值：函数返回值，是返回函数的调用处
# 返回的结果不能直接输出到控制台，需要通过print()才能打印出来
# 1.例一
# def funa():
#     a=10
#     return a
# funa()   #函数调用，把a 返回给funa()  ——————完成了返回的动作，但是没有输出到屏幕上
# print(funa())  #用print()打印出来

# 2.例二  返回多个值
# 返回值本质上只能返回一个值，这个值可以是一个元组，列表，字典等(作为一个整体，当成一个元素来返回）
# 如果返回多个值时，是以元组的形势返回的
# def li2():
#     return 1,2,3
# num=li2()   #调用   1，2，3都返回给li2()
# print(num)  #(1, 2, 3)
# print(type(num))   #<class 'tuple'>

# 3.例三
# def li3():
#     a=5                  #整形
#     b=[1,2]              #列表
#     c={'school':'南汇'}   #字典
#     return a,b,c
# fn=li3()
# print(fn)       #(5, [1, 2], {'school': '南汇'})
# print(type(fn)) #<class 'tuple'>


# ------------------------------------------------------------------------------
# 一个函数里有多个return的情况
# 只有一个return被执行，return表示函数结束，后面的return没什么用处，(函数体内第一个return后面的语句不会执行)
# def funa():
#     return 1
#     return 2
#     print(1,2,3)
# print(funa())    # 1


# ----------------------------------------------------------------------------------
# 一个函数里面没有return的情况 ————实际上也有一个默认的return，即return None
# def showplus1(x):
#     print(x)    # 6 输出结果
#                 #没有写return等效于写了 return None
# num=showplus1(6)
# print(num)      # None

# def showplus2(x):
#     print(x)
#     return x
# num=showplus2(4)
# print(num)




