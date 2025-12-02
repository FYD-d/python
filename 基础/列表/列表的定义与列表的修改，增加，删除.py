# # 列表：一次性存储多个数据
# li=['a','b','c']   # 列表定义：中括号包围所有的元素，每个元素用逗号隔开
# # 特性：有序；  存储多个数据； 元素可以是不同类型
# # li=[2,1.5,'c']
# print(li[0])  #a
# print(li[1])  #b
# print(li[2])  #c
# print(li[-1]) #c

# -----------------------------------------------------------------
#循环读取  for
# li=['a','b','c']
# for i in li:    #可迭代对象 （通过for in 方式能够一个个把元素取出来）
#     print(i)

#while
# li=['a','b','c']
# li_len=len(li)  # len 求列表的元素个数
# i=0
# while i<li_len:
#     print(li[i])
#     i+=1

# --------------------------------------------------------
# 列表操作
# 一.增
# 1) +
# language=['python','c++','java']
# birthday=[1991,1998,1995]
# info=language+birthday
# print(info)

# 2) insert() 插入元素
# 语法:listname.insert(index,object)   表示在index前插入object这个元素
# language=['python','c++','java']
# language.insert(1,'c')
# print(language)
#
# c=('c#','go')
# language.insert(1,c)
# print(language)

# 3)append()末尾追加元素
# 语法：listname.append(obj)  把obj作为整体添加到列表的末尾
# language=['python','c++','java']
# language.append('PHP')
# print(language)
#
# t=('a','v')
# language.append(t)
# print(language)

# 4) extend()
# 语法：listname.extent() 在列表末尾添加obj，并且把obj中的元素拆分成单个
# language=['python','c++','java']
# t=('a','v')
# language.extend(t)
# print(language)


# 二.修改元素：本质是赋值操作
# 1）修改单个元素
# nums=[1,4,3,6,10,8]
# nums[2]=-10  #通过下标访问到指定元素，然后再给指定元素赋新值
# print(nums)

# 2) 修改一组元素
# nums=[1,4,3,6,10,8]
# nums[2:4]=[10,-3,89]  #左右两边个数一致
# print(nums)

#特殊情况：对空切片赋值 （对应下标前插入所有元素）
# nums=[1,4,3,6,10,8]
# # print(nums[4:4])  # []
# nums[4:4]=[-4,25,87]  #从下标为4的前面插入所有元素
# print(nums)

# 三.删除操作
# 1)del   del listname  删除整个列表
# a=list('hello') #把字符串转换成列表
# print(a)   #['h', 'e', 'l', 'l', 'o']
# del a  #整个列表进行删除

# # del listname[index]    通过索引访问值
# a=[1,2,3,4]
# del a[1]
# print(a)

# del  删除多个值
# b=[1,2,3,4,5,6]
# del b[1,3]
# print(b)

# pop()   下标方式删除
# listname.pop(index)   index不写，默认会删除列表中最后一个元素
# nums=[1,2,3,4,5,6,7,8]
# nums.pop(3)
# print(nums)
# nums.pop()
# print(nums)

#listname.remove()   根据元素值进行删除,无则报错
c=[1,2,3,4,5,6,7]
c.remove(4)
print(c)

# listname.clear()  删除列表所有元素
d=[1,22,3,4,4,5]
d.clear()
print(d)









































