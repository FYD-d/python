# 异常：是一个事件，这个事件在程序执行过程中发生，影响了程序的正常运行
# print(a)      #NameError: name 'a' is not defined
# print('a')    #a

# ------------------------------------------------------------------
# 异常处理最终目的：让程序存在异常时，仍能够正常运行
# 异常处理一：try.......except
# 法一
# try:
#    print(a)
# except:   #默认基类异常
#     print('出现错误')
# b=10
# print(b)

# 法二
# try:
#    print(a)
# except NameError as e:   # 指定捕获异常类型为NameError，取名为e
#     print(e)
# b=10
# print(b)

# 法三
# try:
#    print(a)
# except Exception as e:   # 万能异常 Exception 可以捕获任意异常
#     print(e)
# b=10
# print(b)

# 法四：多分枝异常
# try:
#     print(a)
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# except NameError as e:
#     print(e)

# ----------------------------------------------------
# 异常处理格式二：try.....except......else
# else只有在没有异常时才会执行的代码。可以把except理解为if
# dic={'name':'zs'}
# try :
#     print(dict['age'])
# except Exception:
#     print('出现错误')
# else:
#     print('没有捕获到')

# ----------------------------------------------------
# 异常处理格式三： try.....(except)......finally
# finally无论是否出现错误都会执行
# try:
#     print(a)
# except Exception:
#     print('出现错误')
# finally:
#     print('哈哈')

# -------------------------------------------------------
# 异常处理格式三： try.....except......else......finally
try:
    n=int(input('输入一个整数：'))
    print(10/n)
except ValueError:
    print('输入正确数据')
except Exception as e:
    print('未知错误 %s'%e)
else:
    print('无异常才会执行')
finally:
    print('无论有无异常都会执行')















