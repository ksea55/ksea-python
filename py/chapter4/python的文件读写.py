# 读取键盘输入
# Python提供了 input() 内置函数从标准输入读入一行文本，默认的标准输入是键盘。
# input 可以接收一个Python表达式作为输入，并将运算结果返回。


# str = input("请输入你的姓名:")  # 如输入:jacky
# print("您的姓名是:", str, ",请确认!")  # 您的姓名是: jacky ,请确认!

# 读和写文件

"""

open()      将会返回一个 file 对象，基本语法格式如下:

open(filename, mode)
        filename：filename 变量是一个包含了你要访问的文件名称的字符串值。
        mode：mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。

不同模式打开文件的完全列表：
    模式	                                               描述
    
    r   (read)	                                        以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    rb  (read  binary)  	                            以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
    r+  (read +)	                                    打开一个文件用于读写。文件指针将会放在文件的开头。
    rb+	(read binary +)                                 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
    w	(write)                                         打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    wb	(write binary)                                  以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    w+	(write +)                                       打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    wb+	(write binary +)                                以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    a	(append)                                        打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    ab	(append binary)                                 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    a+	(append +)                                      打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    ab+	(append binary +)                               以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
"""


# 简单的一个demo，打开一个文件，将内容写入到该文件中
def demo1(src, model):
    # 打开文件
    srcFile = open(src, "w")  # 在没指定写入的文件编码，将默认采用
    # srcFile = open(src, "w",1,"UTF-8") #指定以UTF-8编码格式写入
    # 写入文件内容
    srcFile.write("大家好,Welcome \n 欢迎Python\n Hello python! \n  very Good!")
    # 关闭资源
    srcFile.close()


# demo1("demo1.txt", "w")  # 调用写入方法




# 上面的demo1将信息写入到文件中，接下来就从文本中读取数据
"""
f.read()
为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
"""


def demo2(fileName, model):
    # 打开要读取的文件
    srcFile = open(fileName, model)  # 在写入文件的是，没有采用编码格式，读取的时候就不需要
    # srcFile = open(fileName, model, 1, "UTF-8") #写入文件的时候使用了编码格式，读取的时候就要采用对应的编码格式

    # 读取的内容
    c = srcFile.read()  # 读取文件中的所有内容，srcFile.read(2)表示每次读取值读取 2个元素
    print("读取到的文件内容是:", c)
    srcFile.close()


# demo2("demo1.txt", "r")



"""

f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
"""


def demo3(srcFileName, model):
    f = open(srcFileName, model)
    context = f.readline()  # 读取文本中的一行数据
    # context=f.readline(2) #读取文本中的一行数据中的2个元素

    print(context)
    f.close()


# demo3("demo1.txt", "r")

# 通过迭代读取文本每行直到末尾行
def demo4(srcFileName, model):
    f = open(srcFileName, model)
    for line in f:
        print(line)
    f.close()


# demo4("demo1.txt", "r")





"""
f.readlines() 将返回该文件中包含的所有行。
如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
"""


def demo5(srcFileName, model):
    f = open(srcFileName, model)
    contxt = f.readlines()
    print(contxt)  # ['大家好,Welcome \n', ' 欢迎Python\n', ' Hello python! \n', '  very Good!']
    f.close()
    return contxt;


contxtList = demo5("demo1.txt", "r")
print(contxtList, len(contxtList), contxtList[0], type(contxtList))
"""
打印结果:
['大家好,Welcome \n', ' 欢迎Python\n', ' Hello python! \n', '  very Good!'] 4 大家好,Welcome 
 <class 'list'>
 
 这个方法很简单, 但是并没有提供一个很好的控制。 因为两者的处理机制不同, 最好不要混用。
"""


# f.write(), f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。

def demo6(srcFileName, model):
    f = open(srcFileName, model)
    contxt = "hello python!"
    num = f.write(contxt)
    print("context is len {0} and num is {1}".format(len(contxt), num))  # context is len 13 and num is 13
    f.close()


# demo6("demo6.txt", "w")




# 如果要写入一些不是字符串的东西, 那么将需要先进行转换:
def demo7(srcFileName, model):
    f = open(srcFileName, model)
    value = ("wwww.baiud.com", 12)
    print(type(value))  # <class 'tuple'>
    v = str(value)  # ('wwww.baiud.com', 12)
    print(v)
    f.write(v)
    f.close()


# demo7("demo7.txt", "w")


# f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
def demo8(srcFileName, model):
    f = open(srcFileName, model)
    v = "welcome ksea!"
    f.write(v)
    position = f.tell()
    print("currentent is position : {0}".format(position))  # currentent is position : 13
    f.close()


# demo8("demo8.txt", "w")


"""

f.seek()
如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)：表示从文件的结尾往前移动x个字符

from_what 值为默认为0，即文件开头。下面给出一个完整的例子：
"""


def demo9(srcFileName, model):
    f = open(srcFileName, model)
    context = "ABCDEFLMNXYZ"
    f.write(context)

    # 获取当前所在的位置
    currPosition = f.tell();
    print("currPosition is  {0}".format(currPosition))  # currPosition is  12
    c = f.read(1)
    print("read context is {0}".format(c))  # read context is

    # 改变指针的指向文本的position
    f.seek(2, 0)
    currPosition = f.tell();
    print("currPosition is  {0}".format(currPosition))  ##currPosition is  0
    c = f.read(1)
    print("read context is {0}".format(c))  # read context is A

    f.close()


demo9("demo9.txt", "w+")

"""
f.close()
在文本文件中 (那些打开文件的模式下没有 b 的), 只会相对于文件起始位置进行定位。
当你处理完一个文件后, 调用 f.close() 来关闭文件并释放系统的资源，如果尝试再调用该文件，则会抛出异常。
>>> f.close()
>>> f.read()
Traceback (most recent call last):
File "<stdin>", line 1, in ?
ValueError: I/O operation on closed file
<pre>
<p>
当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短:</p>
"""


def demo10(srcFileName, m):
    with open(srcFileName, m) as f:
        c = f.read()

    print("读取资源结束!")
    isClose = f.closed
    print("资源文件是否已经关闭:", isClose)  # 资源文件是否已经关闭: True


demo10("demo1.txt", "r")







