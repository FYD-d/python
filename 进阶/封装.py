# 封装：将复杂的信息、流程给包起来，内部处理，让使用者只需要通过简单的操作步骤，就能实现
# 封装的意义：
# 1.将属性和方法放到一起做为一个整体，然后通过实例化对象来处理
# 2.隐藏内部实现细节，只需要和对象及其属性和方法交互就可以了
# 3.对类的属性和方法增加  访问权限控制

# 1.类中封装数据
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def add(self):
#         print(f'姓名是{self.name},年龄是{self.age}')
#
# # 创建对象
# s1=Student('fu',18)
#
# # 通过self间接调用————调用实例方法
# s1.add()
#
# # 通过对象直接调用—————调用属性
# print(s1.name)


# 例：士兵射击
class Soldier:
    def __init__(self,xinghao,zidan):
        self.xinghao=xinghao
        self.zidan=zidan
    def shoot(self):
           if self.zidan <=0:
                print('没有子弹')

           else :
                print(f'{self.xinghao}使用了{self.zidan}发子弹')
                self.zidan-=1

s=Soldier('手枪',20)
s.shoot()
s.shoot()
s.shoot()















