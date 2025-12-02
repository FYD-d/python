# while 条件：
#     while 条件：
#        print('媳妇，我错了')
#     print('罚跪榴莲')

j=0
while j<3:    #连续3天要执行的动作
    i=0
    while i<3:      #每天要说3遍我错了
        print('媳妇，我错了')
        i+=1
    print('罚跪榴莲')
    print('-------惩罚结束-------')
    j+=1

# ----------------------------------------------------------------------------------
# 例1，打印小星星
# print('*'*5)  #字符串的复制
# 把5变成变量i，i代表行数：1<=i<=5
# 法一
i=1
while i<=5:
    print('* '*i)
    i+=1

# # 法二  用循环嵌套
# print()  默认自动换行
# print（'*'，end=' '）  以空格来结尾

row=1  #定义行数初始量
while row<=5:
    col=1    #定义列的初始值
    while col<=row:
        print('*',end=' ')
        col+=1
    print()
    row+=1

# 例2  打印99乘法表
lie=1
while lie<=9:
    hang=1
    while hang<=lie:
        print(f'{hang}*{lie}={lie*hang}',end=' ')
        hang+=1
    print()
    lie+=1








































