#一.公共运算符
# 1.+ 拼接
# # 1）字符串
# str1='aa'
# str2='bb'
# str3=str1+str2
# print(str3)     #aabb
#
# #2) 列表
# list1=[1,2,3]
# list2=[3,4,5]
# list3=list1+list2
# print(list3)      #[1, 2, 3, 3, 4, 5]
#
# #3)元组
# t1=(1,2)
# t2=(2,3)
# t3=t1+t2
# print(t3)       #(1, 2, 2, 3)

# ---------------------------------------------------------------------------
# # 2.* 复制
# # 1)列表
# list1=['hello']
# print(list1*4)      #['hello', 'hello', 'hello', 'hello']
#
# # 2)字符串
# print('*'*10)       #**********

# ---------------------------------------------------------------------------
# # in存在   not in不存在
# list1=['a','b','c']
# print('a'in list1)   #判断结果是True 或False

# =========================================================================================
# 二.公共方法
# 1.len()  计算元素个数    字符串 列表 元组 集合 字典
# #集合举例
# s1={10,20,30}
# print(len(s1))     #3


# # 2.delete()  删除  字符串 列表
# str1='abc'
# del str1     #没有指定删除某个元素，而是删除整个对象，表示删除所有数据，会报错
# print(str1)   #NameError: name 'str1' is not defined


# #3.max()  求最大值
# list1=[10,20,30,40]
# print(max(list1))    #40

# # 4.min() 求最小值
# list1=[10,20,30,40]
# print(min(list1))   #10


# # 5.range()
# for i in range(5):
#     print(i)     #0 1 2 3 4


# # 6.enumerate()  效果是（下标，数据）一一列出，通常用for来遍历
# list1=['a','b','c']
# for i in enumerate(list1):
#     print(i)     #(0, 'a') (1, 'b') (2, 'c')

# -------------------------------------------------------------------------
#三.容器类型推导式
# 列表推导式
## 用while
# list=[]
# i=0
# while i<10:
#     list.append(i)
#     i+=1
# print(list)   #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

##用for
# list=[]
# for i in range(10):
#     list.append(i)
# print(list)   #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


##用列表推导式
# list=[i for i in range(10)]
# print(list)  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

## 元组推导式
# t1=(i for i in range(10))
# print(t1)   #<generator object <genexpr> at 0x000001C1CAAEA890>  返回地址
# print(tuple(t1))   #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

##字典推导式
# dict1={i:i**2 for i in range(5)}  #i:i**2为表达式    for i in range(5)为i的范围
# print(dict1)   #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# # 集合推导式
# list1=[1,2,3]
# set1={i**2 for i in list1}
# print(set1)    #{1, 4, 9}










