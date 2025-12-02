# 异常传递：在主函数中设置“异常捕获”机制，调用子函数
# 例1.
# def funa():     #子函数
#     return int(input('输入整数'))
# def funb():     #主函数
#     return funa()
# try:
#     print(funb())
# except Exception as e:
#     print('错误:%s' % e)

# 例2.
# def test():
#     num=int(input('输入：'))
#     return 10/num
# def test2():
#     print(test())
#
# try:
#     test2()
# except Exception as e:
#     print(f'错误:{e}')

# ---------------------------------------------------------------------
# 抛出异常
# 主动抛出异常的步骤：
# 1.创建一个Exception('...')的对象
# 2.raise 抛出这个对象
# 例一
# def funa():
#     raise Exception('抛出一个异常')
# funa()

# 例二
# def user():
#     pwd=input('请输入一个密码：')
#     if len(pwd)>=6:
#         return pwd
#     else:
#         ex=Exception('长度不够')
#         raise ex
#
# try:
#     a=user()
#     print(a)
# except Exception as e:
#     print('错误%s'%e)

# --------------------------------------------------------
# 模块
# 模块的好处：提高可维护性   可重用  避免函数名和变量名冲突
# 模块分类：
# 1.内置模块（标准库）：python解释器提供
# 查看内置函数
# import builtins
# print(dir(builtins))

# 2.第三方库
# 安装 :
# pip install 模块名

# 3.自定义模块













