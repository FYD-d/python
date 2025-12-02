# 字符编码：本质是二进制数据与语言文字的一一对应关系
# ------------------------------------------------


# 编码，解码
# # encode编码：将字符转换成字节流（二进制数据流）
# a='hello'
# b=b'hello'   字节流
# print(type(a))
# print(type(b))
#
# a='sixstar'
# b=a.encode()  #给a进行编码，把字符串转换成二进制数据流
# print(b)

# decode解码：将字节流转换成字符
# a=b'sixstar'
# b=a.decode()
# print(b)


#--------------------------------------------------------------------
# 索引（下标）：从0开始，范围是左闭右开,超出数据会报错
# name1='abcdef'
# print(name1[0])  #a
# print(name1[1])  #b
#
# name2='uhsddsanvjhalvndjsvndjhvalvndavjfalnasv'
# print(name2[-1])  #倒叙从-1开始

# 小结：用正整数表示索引值，从左向右定位，从0开始计数，如0 1 2
#      用负整数表示索引值，从右向左定位，从-1开始计数，如-1 -2 -3


# ------------------------------------------------------------------------
# 字符串的切片
# name='class_name_sixstar'
# a=name[6]
# b=name[7]
# c=name[8]
# d=name[9]
# print(a+b+c+d)
# print(f'{a}{b}{c}{d}')

# 切片语法：[起始索引：结束索引+1：步长]
name='class_name_sixstar'
print(name[6:10])  #name
print(name[:])  #没有限制去到所有
print(name[-1:3:-1])



























