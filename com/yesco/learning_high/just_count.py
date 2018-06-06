#!usr/bin/python
# -*- coding:UTF-8 -*-

class JustCount:
    '私有，公有属性'
    # 私有属性
    __secretCount = 0
    # 公有属性
    publicCount = 0
    # protect 属性
    _protectCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount
counter = JustCount()
counter.count()
counter.count()
print counter.publicCount
# 下面这种调用行不通，类的实例不能直接引用私有属性
# print counter.__secretCount
print counter._JustCount__secretCount # 间接引用私有属性
