# 元组：不能被修改 ，不能被删除
# 元组的定义：元素由小括号包围，每个元素之间用逗号隔开  如(1,2,3)
# 意义：因为元组不可修改和删除，所以提高了代码编写的安全性。 能用元组的时候，就尽量使用元组

# 验证元组不能被修
# num_list=(10,20,30)
# # print(num_list[0])  #10
# num_list[0]=[10]
# print(num_list)
# TypeError: 'tuple' object does not support item assignment    类型错误：元组类型不支持项赋值

# 验证元组不能被修改
# tuple1=('aa','bb','cc','dd','ee')
# del tuple1 [2]   #尝试删除下标为2的元素
# print(tuple1)
# TypeError: 'tuple' object doesn't support item deletion    类型错误：元组的对象不支持项删除

# ===============================================================================
# 多个数据的元组
# t1=(10,20,30)
# print(t1)

# 定义单个数据的元组，在单元素后面必须加一个逗号
# t2=(10)    #与t2=10 等效
# print(t2)    #10
# print(type(t2))   #<class 'int'>  整形
#
# t3=(10,)
# print(t3)   #(10,)
# print(type(t3))   #<class 'tuple'>

# ====================================================================================
#查找
# 1.通过下标查找
# t1=('sixstar','aa','hfdsj','cc')
# print(t1[1])


# 2.index() 查找某个数据,如果数据存在,在返回对应的下标(索引),否则报错
# t1=('sixstar','aa','hfdsj','cc')
# print(t1.index('aa'))

# 3.count() 统计某个数据在当前元组中出现的个数
# touple.count(obj)  obj为要求统计个数的元素对象,即统计obj在元组出现的次数
# t1=('sixstar','aa','hfdsj','cc','aa')
# print(t1.count('aa'))


# 4.len() 统计元组中数据的个数
t1=('sixstar','aa','hfdsj','cc','aa')
print(len(t1))


# 5.拓展:元组"可变的"情况
t2=(10,20,['sixstar','aa','hfdsj','cc','aa'],40,50)
print(t2[2])   #把中括号看成一个整体,然后通过下标方式取值

# 取中括号中的'aa'
print(t2[2][1])   #aa

# 修改aa
t2[2][1]='hu'
print(t2)  #(10, 20, ['sixstar', 'hu', 'hfdsj', 'cc', 'aa'], 40, 50)


















