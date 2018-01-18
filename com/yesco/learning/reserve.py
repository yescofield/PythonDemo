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

reverse_string = "reverse"

# 字符串反转的3种方法
# 1.切片法（最简洁的一种）
def reverse1(s):
    return s[::-1]

# 2.递归
def reverse2(s):
    if s=="":
        return s
    else:
        return reverse2(s[1:]) + s[0]

# 3.借用列表
# Python中自带reverse()函数，可以处理列表的反转
# join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
# # 如下例子
# str = '-'
# sequence = ('a', 'b', 'c')
# str.join(sequence)
# # 输出结果是：a-b-c
def reverse3(s):
    l = list(s)
    l.reverse()
    return "".join(l)

print '1.切片法:', reverse1(reverse_string)
print '2.递归:', reverse2(reverse_string)
print '3.借用列表:', reverse3(reverse_string)