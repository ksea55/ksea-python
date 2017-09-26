import os

"""
1 os.access(path, mode) 检验权限模式

概述
os.access() 方法使用当前的uid/gid尝试访问路径。大部分操作使用有效的 uid/gid, 因此运行环境可以在 suid/sgid 环境尝试。
语法
access()方法语法格式如下：
os.access(path, mode);
参数
path -- 要用来检测是否有访问权限的路径。
mode -- mode为F_OK，测试存在的路径，或者它可以是包含R_OK, W_OK和X_OK或者R_OK, W_OK和X_OK其中之一或者更多。
os.F_OK: 作为access()的mode参数，测试path是否存在。
os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
os.X_OK 包含在access()的mode参数中 ，测试path是否可执行。
返回值
如果允许访问返回 True , 否则返回False。

"""
fok = os.access("demo1.txt", os.F_OK)
print(fok)  # True

rok = os.access("demo1.txt", os.F_OK)
print(rok)  # True

wok = os.access("demo1.txt", os.W_OK)
print(wok)  # True

xok = os.access("demo1.txt", os.X_OK)
print(xok)  # True

rwx = os.access("demo1.txt", os.F_OK | os.R_OK | os.W_OK)  # 等同于rwx=os.access("demo1.txt",os.F_OK or os.R_OK or os.W_OK)
print(rwx)  # True