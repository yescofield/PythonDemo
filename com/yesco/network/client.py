#!usr/bin/python
# -*- coding:UTF-8 -*-

# 导入 socket 模块
import socket

# 创建一个 socket 对象
s = socket.socket()
# 获取本机IP地址，和server端的一致
host = socket.gethostname()
# 设置端口号
port = 12345
# 连接server端
s.connect((host, port))

print s.recv(1024)

s.send('欢迎光临 client ！')

s.close()
