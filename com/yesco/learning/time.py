#!/usr/bin/python
# -*- coding:UTF-8 -*-

import time # 引入时间模块
import calendar
import datetime

# 时间
ticks = time.time()
print '当前时间戳为：', ticks

localTime = time.localtime(time.time())
print '本地时间为：', localTime

cal = calendar.month(2018, 1)
print "以下输出2016年1月份的日历:"
print cal;

i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)