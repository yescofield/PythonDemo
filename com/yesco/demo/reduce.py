#!usr/bin/python
# -*- coding:UTF-8 -*-

# 分解质因素

def reduceNum(n):
    print '{} = '.format(n),
    if not isinstance(n, int) or n <= 0:
        print '请输入一个正整数'
        exit(0)
    elif n in [1]:
        print '{}'.format(n)

    while n not in [1]:
        for index in xrange(2, n + 1):
            if n % index == 0:
                n /= index
                if n == 1:
                    print '{}'.format(index)
                else:
                    print '{} *'.format(index),
                break


reduceNum(90)
reduceNum(100)

