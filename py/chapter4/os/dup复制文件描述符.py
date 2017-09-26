"""
9 os.dup(fd) 复制文件描述符 fd
语法
dup()方法语法格式如下：
os.dup(fd);
参数
fd -- 文件描述符
返回值
返回复制的文件描述符。

"""
# !/usr/bin/python3

import os, sys

# 打开文件
fd = os.open("dup.txt", os.O_RDWR | os.O_CREAT)
print("fd:", fd)  # 3
# 复制文件描述符
d_fd = os.dup(fd)
print("d_fd:", d_fd)  # 4
# 使用复制的文件描述符写入文件
os.write(d_fd, bytes("This is test", "utf-8"))

# 关闭文件
os.closerange(fd, d_fd)

print("关闭所有文件成功!!")
