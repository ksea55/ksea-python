"""
13 os.fchown(fd, uid, gid) 修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。

概述
os.fchown() 方法用于修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
Unix上可用。
语法
fchown()方法语法格式如下：
os.fchown(fd, uid, gid)
参数
fd -- 文件描述符
uid -- 文件所有者的用户id
gid -- 文件所有者的用户组id
返回值
该方法没有返回值。
"""
# !/usr/bin/python3

import os, sys, stat

# 打开文件 "/tmp/foo.txt"
fd = os.open("/tmp", os.O_RDONLY)

# 设置文件的用户 id 为 100
os.fchown(fd, 100, -1)

# 设置文件的用户组 id 为 100
os.fchown(fd, -1, 50)

print("修改权限成功!!")

# 关闭文件
os.close(fd)
