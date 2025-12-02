# 文件备份思路
# 1) 创建一个新文件，并给它命名
# 2) 读取原文件的内容
# 3) 把读取到的内容写入到新文件中

# 打开文件
f1=open(r'C:\Users\lenovo\OneDrive\Desktop\py\Wilia\wilia.txt','r')       # 打开wilia.txt文件
f2=open(r'C:\Users\lenovo\OneDrive\Desktop\py\Wilia\wilia[副本].txt','w')  # w方式打开时，文件不存在，则会新建

# 读取并写入文件
f1_text=f1.read()    # 读取wilia.txt文件内容
f2.write(f1_text)

# 关闭文件
f1.close()
f2.close()

