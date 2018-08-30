#!usr/bin/python
# -*- coding:UTF-8 -*-

# 水仙花数，153 = 1的三次方 + 5的三次方 + 3的三次方

for n in range(10, 1000):
    i = n / 100
    j = n / 10 % 10
    k = n % 10
    if n == i ** 3 + j ** 3 + k ** 3 :
        print n
