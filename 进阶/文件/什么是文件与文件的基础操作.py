# 1）使用文件的目的
# 把一些内容（数据）存放起来，方便下次程序执行时直接使用，而不必重新制作一份。省时省力

# 2）文件的存储方式
# 在计算机中，文件是以二进制的方式保存在磁盘上的

# 3）文本文件和二进制文件
# 文本文件：可以使用文本编辑软件查看。本质上还是二进制
# 二进制文件：保存的内容不是给人直接阅读的，而是提供给其他软件使用
# 例如：图片软件、音频软件、视频软件


# --------------------------------------------------------------------------
# 文件的操作步骤：
# 1）open：打开文件，并且返回文件的操作对象
# f=open('文件名',‘访问方式’)    #访问方式其实就是文件操作权限
# 对象的属性：
# f.closed 返回的是True，说明文件已被关闭，否则返回False
# f.mode   返回被打开文件的访问模式
# f.name   返回文件的名称

# 2）read(读文件)：将文件内容读取到内存
# read方法执行后，会把文件指针移动到文件的末尾

# 3）write(写文件):将指定内容写入文件

# 4）close:关闭文件

# ------------------------------------------------
# # 1）打开文件
# f=open(r'C:\Users\lenovo\OneDrive\Desktop\py\Wilia\wilia.txt')  # 文件名推荐写完整的文件存放路径
#
# # 2)读取文件
# text=f.read()
# print(text)
# #
# # 3)关闭文件
# f.close()
#
# print('文件名',f.name)
# print('访问模式',f.mode)
# print('是否已关闭',f.closed)


# -----------------------------------------------------
# 基本访问方式
# 读
# f=open(r'C:\Users\lenovo\OneDrive\Desktop\py\Wilia\wilia.txt','r')   #读取wilia.txt的内容
# str=f.read(10)  # 读取前10个字符串
# print('读取的字符串是：',str)
# f.close()

# 写
# f=open(r'C:\Users\lenovo\OneDrive\Desktop\py\Wilia\wilia.txt','w')  # 以写的方式打开
# f.write('welcome')     #welcome要写入这个文件的内容，覆盖写
# f.close()


# 由于文件读写的时候有可能会出现IOError ，一旦出错，f.close()不会被调用。所以为了保证无论是否出错，都能正确地关闭文件，我们可以使用try....finally来实现
# f=open(r'C:\Users\lenovo\OneDrive\Desktop\py\Wilia\wilia.txt','w')
# try:
#     print(f.read())   # 把可能有问题的代码写在try下面
# finally:              # finally 无论前面是否有报错，都会执行的代码
#     f.close()














