#!/usr/bin/python
# -*- coding:UTF-8 -*-

# I/O学习
# 打印到屏幕，print
print '不是吗？'

# 读取键盘输入raw_input、input
# raw_input: 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）
string = raw_input('请输入：')
print '您输入的内容是：', string

# input: 和raw_input([prompt])函数基本类似，可以接收一个Python表达式作为输入，并将运算结果返回。
# 输入：[x*5 for x in range(2,10,2)]
# 输出结果是： [10, 20, 30, 40]
string = input("请输入：")
print "您输入的内容结果是：", string

# 打开和关闭文件
