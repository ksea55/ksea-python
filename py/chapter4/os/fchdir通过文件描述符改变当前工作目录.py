"""
11 os.fchdir(fd) 通过文件描述符改变当前工作目录
概述
os.fchdir() 方法通过文件描述符改变当前工作目录。
Unix, Windows 上可用。
语法
fchdir()方法语法格式如下：
os.fchdir(fd);
参数
fd -- 文件描述符
返回值
该方法没有返回值。
"""
# !/usr/bin/python3

import os,sys

# 首先到目录 "D:\activeMQ\apache-activemq-5.14.5\examples\amqp\python"
os.chdir(r"D:\activeMQ\apache-activemq-5.14.5\examples\amqp\python")

# 输出当前目录
print("当前工作目录为 : %s" % os.getcwd())

# 打开新目录 "/tmp"
fd = os.open(r"D:\a\a.txt",os.O_RDONLY)
print(fd)
# 使用 os.fchdir() 方法修改到新目录
#os.fchdir(fd) #AttributeError: module 'os' has no attribute 'fchdir'

# 输出当前目录
print("当前工作目录为 : %s" % os.getcwd())

# 关闭打开的目录
os.close(fd)
