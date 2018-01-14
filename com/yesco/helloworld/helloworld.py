#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 同一行显示多条语句, 注意：因为有import，所以需要置顶
# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# 行和缩进，区域快
if True:
    print "hello python true";
else:
    print "hello python false";

# 等待用户输入
# raw_input("\n\nPress the enter key to exit.")

name = "Madisetti" # 这是一个注释
# 多行注释
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
'''
# Python语句中一般以新行作为为语句的结束符。
# 但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：
total = item_one + \
        item_two + \
        item_three
'''

# 语句中包含[], {} 或 () 括号就不需要使用多行连接符。如下实例：
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

# Python 接收单引号(' )，双引号(" )，三引号(''' """) 来表示字符串，引号的开始与结束必须的相同类型的。
# 其中三引号可以由多行组成，编写多行文本的快捷语法，常用语文档字符串，在文件的特定地点，被当做注释。
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""

# 多个语句构成代码组
if True :
    print "hello python 1";
elif True :
    print "hello python 2";
else :
    print "hello python 3";