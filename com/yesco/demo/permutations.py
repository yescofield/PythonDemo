#!/usr/bin/python
# -*- coding:UTF-8 -*-

# ....1....permutations
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

count = 0   # 直接计数
d = []      # 利用列表计数
for index_i in range(1, 5):
    for index_j in range(1, 5):
        for index_k in range(1, 5):
            if(index_i != index_k) and (index_i != index_j) and (index_k != index_j):
                count += 1
                d.append([index_i, index_j, index_k])
                print index_i, index_j, index_k
print '一共有 ', count, ' 个'
print '一共有 ', len(d), ' 个'


from itertools import permutations

count = 0
for i in permutations([1, 2, 3, 4], 3):
    count += 1
    print i
print '一共有 ', count, ' 个'
