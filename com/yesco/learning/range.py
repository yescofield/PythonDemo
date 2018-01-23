#!/usr/bin/python
# -*- coding:UTF-8 -*-

# range函数的使用学习
# range() 函数可创建一个整数列表，一般用在 for 循环中。
# range(start, stop[, step])
# 参数说明：
# start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# end: 计数到 end 结束，但不包括 end。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

# 输出的是：0 1 2 3 4
for i in range(5):
    print i

# 输出的是：0 1 2 3 4
for i in range(0, 5):
    print i

# 输出的是：0 2 4
for i in range(0, 5, 2):
    print i

# 打印九九乘法表
print '\n'.join(['\t'.join(['%d * %d = %d' % (y, x, x*y) for y in range(1,x+1)])for x in range(1, 10)])