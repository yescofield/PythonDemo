#!/usr/bin/python
# -*- coding:UTF-8 -*-

print 'hello, 列表翻转函数实现'


def reverse(li):
    for i in range(0, len(li)/ 2):
        temp = li[i]
        li[i] = li[-i - 1]
        li[-i - 1] = temp

l = [1, 2, 3, 4, 5]
print 'l列表翻转之前:', (l)
reverse(l)
print 'l列表翻转之后:', (l)

# str = 'reverse'
# print 'str翻转之前:', (str)
# reverse(l)
# print 'str翻转之后:', (str)

str = '1234567'
str2l = [int(x) for x in str[::-1]]
print 'str翻转之前:', (str2l)
reverse(str2l)
print 'str翻转之后:', (str2l)