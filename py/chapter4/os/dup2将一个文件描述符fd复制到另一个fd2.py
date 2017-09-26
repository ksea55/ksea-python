""" 
10 os.dup2(fd, fd2) 将一个文件描述符 fd 复制到另一个 fd2
概述
os.dup2() 方法用于将一个文件描述符 fd 复制到另一个 fd2。
Unix, Windows 上可用。
语法
dup2()方法语法格式如下：
os.dup2(fd, fd2);
参数
fd -- 要被复制的文件描述符
fd2 -- 复制的文件描述符
返回值
没有返回值。
"""
# !/usr/bin/python3

import os

# 打开文件
fd = os.open("dup2.txt", os.O_RDWR | os.O_CREAT)

# 写入字符串
os.write(fd, bytes("This is test", "utf-8"))
print("复制之前的fd:", fd)

# 文件描述符为 1000
fd2 = 1000
os.dup2(fd, fd2);

print("执行dup2之后的fd2:", fd2)

# 在新的文件描述符上插入数据
os.lseek(fd2, 0, 0)
str = os.read(fd2, 100)
print("读取的字符串是 : ", str)

# 关闭文件
os.close(fd)

print("关闭文件成功!!")
"""
打印结果:
复制之前的fd: 3
执行dup2之后的fd2: 1000
读取的字符串是 :  b'This is test'
关闭文件成功!!
"""
