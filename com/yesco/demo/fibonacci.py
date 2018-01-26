#!usr/bin/python
# -*- coding:UTF-8 -*-

# 题目：斐波那契数列，经典的递归
# 解析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……
# 在数学上，费波那契数列是以递归的方法来定义：
# F0 = 0    (n=0)
# F1 = 1    (n=1)
# Fn = F[n-1] + F[n-2]  (n>=2)

def Fibonacci(n):
    ' n 指的是自然数，从1开始，也就是第几个斐波那契数的意思'
    if (n == 1) or (n == 2):
        return n - 1
    else :
        return Fibonacci(n - 1) + Fibonacci(n - 2)

print '第1个数：', Fibonacci(1)
print '第2个数：', Fibonacci(2)
print '第10个数：', Fibonacci(10)
