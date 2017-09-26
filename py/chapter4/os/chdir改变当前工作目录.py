import  os
"""
2 os.chdir(path) 改变当前工作目录

概述
os.chdir() 方法用于改变当前工作目录到指定的路径。

语法
chdir()方法语法格式如下：

os.chdir(path)

参数
path -- 要切换到的新路径。
返回值
如果允许访问返回 True , 否则返回False。

"""
# 获取当前路径
currPath = os.getcwd()
print("currPath: ", currPath)  # currPath:  D:\ksea\ksea-python\py\chapter4

# 将其当前路径改变到chPath路径
chPath = "D:\ksea\ksea-python\py\chapter2"
os.chdir(chPath)
# 获取改变之后的路径
print("changePath: ", os.getcwd())  # changePath:  D:\ksea\ksea-python\py\chapter2