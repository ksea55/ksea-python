# 这里主要讲解说明在python中的基础语法

#一、python中的保留关键字

# python保留字
# 保留字即关键字，我们不能把它们用作任何标识符名称。Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：
# >>> import keyword
# >>> keyword.kwlist
# 输出内容: ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']






#二、python中的注释单行注释以及多行注释

# >>> Python中单行注释以 # 开头，实例如下：

# 第一个注释
print("Hello, Python!")  # 第二个注释
# 执行以上代码，输出结果为：
# Hello, Python!

# 多行注释可以用多个 # 号：

# 第一个注释
# 第二个注释

print("Hello, Python!")
# 执行以上代码，输出结果为：
# Hello, Python!







#三、python中的代码【行与缩进】

# python最具特色的就是使用缩进来表示代码块，不需要使用大括号({})。
# 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
if True:
    print("this is True");
else:
    print("this is False");

# 以下代码最后一行语句缩进数的空格数不一致，会导致运行错误：
#if True:
#    print("Answer")
#    print("True")
#else:
#    print("Answer")
#  print("False")#这里的缩进与else或者print("Answer")并为保持一致，所以在运行报错
#异常信息如下
#File "D:/ksea/ksea-python/py/chapter1/basePython.py", line 46
#print("False")
#IndentationError: unindent does not match any outer indentation level  取消缩排不匹配任何外部的缩进级别





# 四、python中的多行语句拼接

#这里我们在拼接多个字符串，需换行拼接的使用需要跟上 + \ 并且这里一定要注意【缩进】
say="this " + \
     "is "  + \
     "python"
print(say);

#在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']
print("数字长度:"+str(total.__len__())+" ,数组数据: "+str(total))
#此处在打印字符串时，因为类型缘故，还需要用到str()方法，将其转换成字符串




#五、python中的数据类型，python中数有四种类型：整数、长整数、浮点数和复数。
#整数， 如 1
a=1;
print(a)
#长整数 是比较大的整数
b=342342344444444444444444444444444444444;
print(b)
#浮点数 如 1.23、3E-2
c=1.23;
d=3E-2;
print(str(c)+"---"+str(d)); #打印结果:1.23---0.03
#复数 如 1 + 2j、 1.1 + 2.2j
e=1+2j;
f=1.1+2.2j;
print(str(e)+"--"+str(f));




#六、python中的字符串

#python中单 引号'' 和 双引号 "" 使用完全相同。
a1='this is a1'
a2="this is a2"
print(a1+"--"+a2)

#注意在使用三引号(''' 或 """)可以指定一个多行字符串。
a3=''' 第一行
第二行
第三行
第四行'''

print(a3)
a4="""
this
is
many
rows
string
""";
print(a4)

#转义符 '\'
a5="\"this is quote\"";
print(a5) #打印结果: "this is quote"
#自然字符串， 通过在字符串前加r或R。 如 r"this is a line with \n" 则\n会显示，并不是换行。

a6="this is a line \n say hello"
print(a6)
#打印结果:
# this is a line
#   say hello

a7=r"this is a line \n say hello"
print(a7) #打印结果:this is a line \n say hello

#python允许处理unicode字符串，加前缀u或U， 如 u"this is an unicode string"。

a8=U"this is a line  say hello"
print(a8)
#注意，字符串是不可变的。

#按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
a9= "this "  "is " "string "
print(a9)#打印结果:this is string  这里也可以用+连接结果一样

#word = '字符串'
#sentence = "这是一个句子。"
#paragraph = """这是一个段落，




#七、空行的作用
#函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
#空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
#记住：空行也是程序代码的一部分。




#八、等待用户输入指令函数input
#执行下面的程序在按回车键后就会等待用户输入：

#input("\n\n按下 enter 键后退出。")




#九、python中同一行可以显示多条语句
#Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
import sys; x = 'runoob'; sys.stdout.write(x + '\n')




#十、python中的Print 输出
#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：

x="a"
y="b"
# 换行输出
print( x )
print( y )

print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )




#十一、import 与 from...import
#在 python 用 import 或者 from...import 来导入相应的模块。
#将整个模块(somemodule)导入，格式为： import somemodule
#从某个模块中导入某个函数,格式为： from somemodule import somefunction
#从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
#将某个模块中的全部函数导入，格式为： from somemodule import *】




#十二、在 Windows 下可以不写第一行注释:
#!/usr/bin/python3
#第一行注释标的是指向 python 的路径，告诉操作系统执行这个脚本的时候，调用 /usr/bin 下的 python 解释器。
#此外还有以下形式（推荐写法）：
#!/usr/bin/env python3
#这种用法先在 env（环境变量）设置里查找 python 的安装路径，再调用对应路径下的解释器程序完成操作。