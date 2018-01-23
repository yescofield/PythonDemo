#!/usr/bin/python
# -*- coding:UTF-8 -*-

# join函数的使用学习
# string.join(seq)
# 以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

str = '-'
sequence = ('a', 'b', 'c')
str.join(sequence)
# 输出结果是：a-b-c

# 打印九九乘法表
print '\n'.join(['\t'.join(['%d * %d = %d' % (y, x, x*y) for y in range(1,x+1)])for x in range(1, 10)])