#!usr/bin/python
# -*- coding:UTF-8 -*-

# 暂停一秒输出格式化的当前时间

import time

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

time.sleep(1)

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
