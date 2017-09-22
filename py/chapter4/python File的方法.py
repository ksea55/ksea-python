""" 
Python3 中操作 File(文件) 的 方法

file 对象使用 open 函数来创建，下表列出了 file 对象常用的函数：

file.close()    关闭文件。关闭后文件不能再进行读写操作。

file.flush()    刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。

file.fileno()   返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。

file.isatty()   如果文件连接到一个终端设备返回 True，否则返回 False。

file.next()     返回文件下一行。

file.read([size])   从文件读取指定的字节数，如果未给定或为负则读取所有。

file.readline([size])   读取整行，包括 "\n" 字符。

file.readlines([sizeint])   读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。

file.seek(offset[, whence]) 设置文件当前位置

file.tell()     返回文件当前位置。

file.truncate([size])   从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后 V 后面的所有字符被删除，其中 Widnows 系统下的换行代表2个字符大小。

file.write(str) 将字符串写入文件，没有返回值。

file.writelines(sequence)   向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
"""



import os
import os.path

#path = 'D:/UC/'
ls = []

def getAppointFile(path,ls):
    fileList = os.listdir(path)
    try:
        for tmp in fileList:
            pathTmp = os.path.join(path,tmp)
            if True==os.path.isdir(pathTmp):
                getAppointFile(pathTmp,ls)
            elif pathTmp[pathTmp.rfind('.')+1:].upper()=='PY':
                ls.append(pathTmp)
    except PermissionError:
        pass

def main():

    while True:
        path = input('请输入路径:').strip()
        if os.path.isdir(path) == True:
            break

    getAppointFile(path,ls)
    #print(len(ls))
    print(ls)
    print(len(ls))

main()