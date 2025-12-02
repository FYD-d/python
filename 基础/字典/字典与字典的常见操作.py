# 一.字典的应用场景
## 存储多个数据
# list=['Tom' ,'男',20]
# # 取数‘Tom’
# print(list[0])

# 字典特性：键值对成对出现，键和值一一映射，绑定的关系
# 所以字典的数据和数据顺序没有关系，即字典不支持下标，后期无论数据如何变化，只需要按照对应的键来查找数据即可

# ==================================================================================
# 二.字典定义
# 符号是大括号 ;数据为“键值对”形式出现 ;各个键值对之间用逗号隔开
# 键值对成对出现，键和值一一映射，绑定的关系     key：value
# 重点：key是唯一
## 举例
# dict={'name':'Tom' ,'age':20,'gender':'男'}
# print(dict['name'])

# 定义空字典
## 法一
# dict2={}

## 法二
# dict3=dict()

# ========================================================================================
# 三.常见操作
# 1.修改——有则覆盖（修改）
# dict1={'name':'Willia','age':18,'gender':'女孩'}
# dict1['name']='Tom'
# print(dict1)

# 2.增  添加元素——无则添加
# dict1={'name':'Willia','age':18,'gender':'女孩'}
# dict1['id']=110
# print(dict1)

# 小结：对于key，无则添加，有则覆盖（修改）

# 3.删除
# 1)del 删除方式
# dict1={'name':'Willia','age':18,'gender':'女孩'}
# del dict1['age']
# print(dict1)

# 2）clear() 清空字典
# dict1={'name':'Willia','age':18,'gender':'女孩'}
# dict1.clear()
# print(dict1)

# 4.查
#1)通过key值来查找
# dict={'name':'Tom' ,'age':20,'gender':'男'}
# print(dict['name'])

#2)len()查找键值对个数
# dict={'name':'Tom' ,'age':20,'gender':'男'}
# print(len(dict))

#3)dict.keys()查找所有键,返回列表
# dict={'name':'Tom' ,'age':20,'gender':'男'}
# print(dict.keys())

#4)dict.values()查找所有值，返回列表
# dict={'name':'Tom' ,'age':20,'gender':'男'}
# print(dict.values())

#5)dict.items()查找所有键和值
# dict = {'name': 'Tom', 'age': 20, 'gender': '男'}
# print(dict.items())

# =====================================================================
# 四.字典遍历
# 循环遍历value
dict = {'name': 'Tom', 'age': 20, 'gender': '男'}
for i in dict.values():
    print(i)

# 循环遍历item
dict = {'name': 'Tom', 'age': 20, 'gender': '男'}
for item in dict.items():
    print(item)

# 循环输出  key=value
dict = {'name': 'Tom', 'age': 20, 'gender': '男'}
for key,value in dict.items():
    print(f'{key}={value}')










