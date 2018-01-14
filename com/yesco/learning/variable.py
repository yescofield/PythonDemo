#!/usr/bin/python
# -*- coding:UTF-8 -*-

# 变量赋值
counter = 800  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print counter
print miles
print name
print '*************************************'
# 多个变量赋值
# 创建一个整型对象，值为1，三个变量被分配到相同的内存空间上
a = b = c = 1
print a, b, c
# 多个对象指定多个变量, 两个整型对象1和2的分配给变量a和b，字符串对象"john"分配给变量c
a, b, c = 1, 2, "John"
print a, b, c
print '*************************************'
# for循环
for letter in 'Python':    # 第一个实例
    print '当前字符：' + letter
print '*************************************'
fruits = ['banana', 'apple', 'mango']
for fruit in fruits:      # 第二个实例
    print '当前水果：', fruit
print '*************************************'
for index in range(len(fruits)):     # 通过序列索引迭代
    print '当前水果：', fruits[index]
print '*************************************'
# 循环使用 else 语句
for num in range(10, 20):      # 迭代 10 到 20 之间的数字
    for i in range(2, num):      # 根据因子迭代
        if num % i == 0:    # 确定第一个因子
            j = num / i     # 计算第二个因子
            print '%d 等于 %d * %d'%(num, i, j)
            break       # 跳出当前循环
    else:      # 这里的else并不是上面if的否则，而是上面for循环的判定条件的否则
        print num, '是一个质数'
print '*************************************'
# while循环
count = 0
while count < 3 :
    print 'count = ', count
    count += 1
print '*************************************'
# continue 用法,跳出此次循环语句
i = 1
while i < 5:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print i  # 输出双数2、4、6、8、10
print '*************************************'
# break 用法,终止循环语句
i = 1
while 1:  # 循环条件为1必定成立
    print i  # 输出1~10
    i += 1
    if i > 5:  # 当i大于10时跳出循环
        break
print '*************************************'
# pass语句。pass是空语句，是为了保持程序结构的完整性。不做任何事情，一般用做占位语句。
for letter in 'Python':
    if letter == 'h':
        pass
        print '这是 pass 语句'
    print letter

# 在内存中存储的数据可以有多种类型。
# 例如，person.s年龄作为一个数值存储和他或她的地址是字母数字字符存储。
# Python有一些标准类型用于定义操作上，他们和为他们每个人的存储方法可能。
# Python有五个标准的数据类型：
# Numbers（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Dictionary（字典）