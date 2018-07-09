#!usr/bin/python
# -*- coding:UTF-8 -*-

# 导入 socket 模块
import socket
# 创建一个 socket 对象
s = socket.socket()
# 获取本机IP地址
host = socket.gethostname()
# 设置端口
port = 12345
# 绑定端口
s.bind((host, port))

# 等待客户端连接
s.listen(5)

while True:
    # 建立客户端连接
    c, address = s.accept()
    print '连接地址：', address
    c.send('欢迎光临 server！')

    print c.recv(1024)
    # 关闭连接
    c.close()
