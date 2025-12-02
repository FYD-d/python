# in 存在，在....里面 True   否则为False
# not in 不在....里面 True  否则为False
from operator import index

# list1=['1','2','hello']
# name=input('需要查找的元素是：')
# if name in list1:
#     print('YES')
# else:
#     print('NO')


# count() 用来统计某个元素在列表中出现的次数
# listname.count(obj)  #obj表示要统计的元素
# count 如返回0，则表示不存在这个元素---可用count方法来判断某个元素是否存在
# nums=[1,2,3,4,5,6,7,2,2]
# print(nums.count(2))
# if nums.count(100)>1:
#     print('yes')
# else:
#     print('no')

# ====================================================================
# index()  查找某个元素在列表中出现的位置
# 语法 listname.index(obj,star,end)
# nums=[1,2,3,4,5,6,7,2,2]
# print(nums.index(3))  #查找3对应的下标

# ==========================================================================
# reverse()  把原列表顺序倒置
# li1=[1,2,4,3]
# print(li1)
# li1.reverse()
# print(li1)


# sort()  排序 从下到大升序排列
# li1=[1,2,4,3]
# li1.sort()
# print(li1)
#
# li1.sort(reverse=True)  #从大到小降序排列
# print(li1)

# 拓展
# sort只应用于list的方法
# sorted() 内建函数
li1=[1,2,4,3]
b=sorted(li1)  #默认从小到大排序  不对原列表进行修改
print(b)
print(li1)

li1.sort()
print(li1)   #对原列表进行修改，就地排序无返回值。 如果和赋值，打印等方法一起使用，结果会返回None

# =========================================================
# 列表推导式
# li=[1,2,3,4,5,6,7,8,9]
# print([i*2 for i in li ])  #元素为表达式的值(i*2),i的取值来自于li列表

# for循环
# li=[1,2,3,4,5,6,7,8,9]
# li2=[]
# for i in li:   #i取值范围来自于li
#     li2.append(i*2)   #在列表末尾添加元素 i*2
# print(li2)

#while循环
# li=[1,2,3,4,5,6,7,8,9]
# li2=[]
# i=1
# while i <=len(li):
#     li2.append(i*2)
#     i+=1
# print(li2)


















































