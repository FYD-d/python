# 字符串查找
# find     字符串序列.find（str，开始下标，结束下标）
# 检查字串str是否包含在原字符串myst中，如果在则返回第一次找到的索引值，否则返回-1
# a='hello world'
# print(a.find('hello'))  #返回第一次找到时的索引值（最开始的索引值： h  ）
# print(a.find('l',1,5))

# ------------------------------------------------------------------------
# index 查找索引
# index     字符串序列.index（str，开始下标，结束下标）
# a='hello world'
# print(a.index('l',0,3))

# ---------------------------------------------------------------------------
# count查找字串在原字符串中出现的次数
# count     字符串序列.count（str，开始下标，结束下标）
# a='hello world'
# print(a.count('l',1,5))

# --------------------------------------------------------------------
# 字符串修改
# 1.replace
# 字符串序列.replace（旧字串，新字串，替换次数）
# a='hello world'
# print(a.replace('l','a',))
# print(a.replace('l','a',2))

# 2.split 分割
# 字符串序列.split（str，切的次数）  用str来切原字符串
a='hello world'
print(a.split(' '))

# 3.capitalize 把第一个字母变成大写
# a='hello world'
# print(a.capitalize())

# 4.lower 把字符串所有大写转会为小写
# a='HELLO'
# print(a.lower())

# 5.upper 把字符串所有小写转会为大写
# a='hello'
# print(a.upper())

# 6.title 把字符串的每个单词首字母大写
# a='hello world'
# print(a.title())

# ---------------------------------------------------------------
# 判断
# 1.islower（）检测字符串是否都由小写字母来组成
# a='hello python'
# print(a.islower())
# b='Hello python'
# print(b.islower())

# 2.isupper（）检测字符串是否都由大写字母来组成
# a='HELLO'
# print(a.isupper())

# 3.isdigit() 检测字符串是否都由数字来组成

a='hello123'
i=0
for i in a :
    if a.isdigit():
        i=i+1  #统计数字的个数
print(i)   #包含数字的个数

# 小结：通过上述方式，可以判断字符串大写，小写，数字及其他字符的个数

# 4.startswith() 判断字符串是否带着什么开头
a='hello'
print(a.startswith('h'))

# 5.endswith() 判断字符串是否带着什么结尾
a='hello'
print(a.endswith('o'))

# ------------------------------------------------------------------
# 增
# 1.+
name='six'
name2='star'
info=name+name2
print(info)

# 2.join
a='hello'
print('*'.join(a))

# 删
# 1.lstrip()  删除字符串左边的空白字符
a='hello'
print(a.lstrip())
print(a.lstrip('h'))

# 2.rstrip()  删除字符串右边的空白字符
a='hello'
print(a.lstrip())
print(a.rstrip('o'))

# 3.strip()  删除字符串两边的空白字符
a='  hello  '
print(a)
print(a.strip())

































