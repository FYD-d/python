# 面向过程：需要实现一个功能时，着重的是开发的步骤和过程，每个过程需要自己亲历亲为，需要编写代码（自己来做）
# 面向对象：需要实现一个功能时，不注重开发的步骤和过程，关心的是谁来帮我做这件事
# 面向对象的程序设计的核心是对象（上帝思维），要理解对象为何物，必须把自己当成上帝，上帝眼里世间存在的万物皆为对象，不存在的也可以创造出来

# --------------------------------------------------------------------------------------------------------
# 类：抽象概念----有相同属性和功能的一类事物 （模板）
# 对象：类的具体表现，是面向对象编程的核心---具体  （根据模板造出来的具体东西）

# 类的定义
# 使用class（类）关键字
# 1.
# class 类名：    （类名习惯使用驼峰命名法————首字母大写，私有类可用一个下划线开头）
#     pass     #里面什么都没有，可用pass
# 2.
# class 类名：
#      成员
class Hero(object):     #object 是python里所有类最顶级父类
    def info(self):     #info是实例方法，第一个参数一般是self ，表示的是实例本身，也可取其他名字，其作用是这个变量指向了实例对象
        print('hero')

# -------------------------------------------------------------------------------
# 属性：对象的特征描述（实际上为类中定义的变量，该变量为属性）
# 方法： 对象具有的行为（本质是函数），类中定义的函数即方法
class Student():
    name='lucy'      #属性
    def info(self):  #方法
        print(123)

# print(Student.__dict__)   #查看类的属性
# print(Student.__dict__['name'])  #查看单个属性  lucy

# 增删改查类中的单个属性
# print(Student.name)

# Student.name='哈哈'  #修改
# print(Student.name) #修改之后，属性内容变为哈哈

# del Student.name   #删除属性
# print(Student.name) #AttributeError: type object 'Student' has no attribute 'name'   删除成功

# Student.walk='走路'  #新增属性
# print(Student.walk)

# 小结：属性有则覆盖，无则添加，使用的是 类名.s属性


# -------------------------------------------------------------------
# 对象的创建
# 创建对象的格式：对象名=类名()   实例化了一个对象
# class Hero():
#     def info(self):    #实例方法
#         print(self)
#         print('self各不同，对象是出处')
# # 创建对象，实例化一个对象。 也可以理解为是一个对象的定义
# hero1=Hero()    #创建的对象不限制数量
# hero2=Hero()
# hero3=Hero()
# hero1.info()     #调用实例方法    <__main__.Hero object at 0x0000024AB7FA5C10>
# print(hero1)     #打印的是内存地址 <__main__.Hero object at 0x0000022592205C10>
# hero2.info()     #<__main__.Hero object at 0x0000024AB82722E0>
# hero3.info()     #<__main__.Hero object at 0x0000024AB80EE9A0>
















