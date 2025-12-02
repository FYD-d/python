# %s:字符串
# %d:整数
# %f:小数

'大家好，我叫小溪，今年18岁，身高185，体重40.5kg'
name='小溪'
age=18
height=185
kg=40.5
print('大家好，我叫%s，今年%d岁，身高%d，体重%.1fkg'%(name,age,height,kg))
print('大家好，我叫{}，今年{}岁，身高{}，体重{}kg'.format(name,age,height,kg))
print(f'大家好，我叫{name}，今年{age}岁，身高{height}，体重{kg}kg')
