#!/usr/bin/python
# -*- coding:UTF-8 -*-

# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 分析：m月n日，就是把m-1月之前的天数计算出来，然后加上n天即可。
# 但是需要考虑闰年，也就是2月只有29天的情况，所以如果是闰年且大于2月直接加一天即可

def isLeapYear(year):
    "判断是否是闰年"
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return 1
    else:
        return 0
# 12个月分别对应的天数，二月暂且用28天计算，然后判断是否是闰年的问题
months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

year = input("请输入年份：")
if (year < 1950) or (year > 3000):
    year = input("请输入1950-3000之间的年份：")
month = input("请输入月份：")
if (month < 1) or (month > 12):
    month = input("请输入有效的月份：")
day = input("请输入日：")
day_min = 1
day_max = 31
# 判断输入的日期是否有效
if (isLeapYear(year) == 1) and (month == 2):
    day_max = 29
else:
    day_max = months[month-1]
if (day < day_min) or (day > day_max):
    day = input("请输入有效的日期：")

sum = 0
for index in range(0, month - 1):
    sum += months[index]
sum += day
if (isLeapYear(year) == 1) and (month > 2):
    sum += 1

print '输入的日期是%d年的第%d天'%(year, sum)

