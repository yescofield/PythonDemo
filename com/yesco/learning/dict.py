#!/usr/bin/python
# -*- coding:UTF-8 -*-

# 访问字典
dict = {'Alice': '123', 'Banana': '456', 'Apple': '789'}
print dict['Alice']

dict1 = {'abc': 12.3, 'Banana': 13.45, 'Apple': 7.89}
print dict1['Banana']

# 修改字典
dict['Banana'] = '111'
dict['School'] = 'Peking'
print dict['Banana']
print dict['School']

# 删除字典元素
del dict['Alice']
dict.clear()
del dict
# print dict['Banana'] #因为上面已经用del删除了字典，所以这里再访问就会报错

# 字典键的特性
# 1.不允许同一个键出现两次。出现多次以最后一个出现的值被记住
# 2.键必须不可变，所以可以用数字、字符串或者元组充当。所以用列表就是不行
