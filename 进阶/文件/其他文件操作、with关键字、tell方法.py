# 上面讲的默认读取的是文本文件，UTF—8 文本文件
#
# f=open(r'C:\Users\lenovo\OneDrive\Desktop\py\Wilia\wilia.txt','r',encoding='utf-8')
# content=f.read()
# print(content)

# 二进制方式读取文件   (二进制不支持中文)
# f=open(r'C:\Users\lenovo\OneDrive\Desktop\py\Wilia\wilia.txt','rb')
# content=f.read()
# print(content)
# 把二进制的内容转换成字符串 （解码）
# content=content.decode('utf-8')
# print(content)
# f.close()


# ------------------------------------------------------------------
# with :作用同try.....finally.....
# 如果在调用write的过程中，出现了异常导致后续代码无法运行，从而close方法也无法正常调用。此时资源会一直被占用。
# 可以用with来保证出现错误时，保证代码能正常运行
# with 上下文管理器
# with 的好处：使用完文件会自动将文件进行关闭，无需手动调用close方法

# with open(r'C:\Users\lenovo\OneDrive\Desktop\py\Wilia\wilia.txt','r') as f:   # as 取别名
#     print(f.read())            # 读取willia.txt文件
#
#
# print(f.closed)  # 文件关闭状态 True


# -----------------------------------------------------
# tell() 方法告诉你文件的当前位置。下一次操作从当前位置开始
# seek(offset,[,from]) 改变当前文件的位置 (改变指针位置)。 offset开始的偏移量，from指定开始移动字节的参考位置
# seek(2,1)  从1这个位置开始偏移2个量

f=open(r'C:\Users\lenovo\OneDrive\Desktop\py\Wilia\wilia.txt','r')
text=f.read(10)
print('读取的字符串是：',text)

# 查找当前位置
position=f.tell()
print('当前文件的位置：',position)

# 把指针重新定位到文件开头
position=f.seek(0,0)
text2=f.read(10)
print('重新读取的字符串是:',text2)

# 关闭文件
f.close()

































