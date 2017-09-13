# Python3 中有六个标准的数据类型：
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Sets（集合）
# Dictionary（字典）

# 此处说明String

# String（字符串）
# Python中的字符串用单引号(')或双引号(")括起来，同时使用反斜杠(\)转义特殊字符。
# 字符串的截取的语法格式如下：
# 变量[头下标:尾下标]
# 索引值以 0 为开始值，-1 为从末尾的开始位置。
# 加号 (+) 是字符串的连接符， 星号 (*) 表示复制当前字符串，紧跟的数字为复制的次数。实例如下：


mystr = "ABCDEFG"  # 声明一个字符串
print(mystr)  # 打印字符串，打印结果:ABCDEFG
print(mystr[0])  #:打印结果:A    0取正向顺序的第一个值
print(mystr[-1])  # 打印结果:G  -1取逆向顺序的第一个值
print(mystr[0:])  # 打印结果：ABCDEFG  表示从0开始取所有的
print(mystr[1:])  # 打印结果：BCDEFG  这种取值方式，是包含当前索引值 也就是包含当前1所在索引的值
print(mystr[0:2])  # 打印结果:AB 这种结果是包前不包后的，也就是包含索引0所在的值，不包含截止值2索引所在的值
print(mystr[0:-1])  # 打印结果:ABCDEF
print(mystr * 3)  #:打印结果：ABCDEFGABCDEFGABCDEFG  *表示复制其当前的字符串  3 表示复制当前字符串的次数

# Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
print('Ru\noob')
""" 打印结果：Ru
            oob  此处\n表示换行"""
# 如果你不想特殊字符被转移 你可以在当前字符串前面加上r或者R
print(r'Ru\noob')  # 打印结果:Ru\noob

# Python 没有单独的字符类型，一个字符就是长度为1的字符串。
# 实例
word = 'Python'
print(word[0], word[5])  # 打印结果:P n

print(word[-1], word[-6])  # 打印结果:n P

# 与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。
# word[0]="b"
"""
报错信息如下:
  word[0]="b"
ABCDEFG
TypeError: 'str' object does not support item assignment
"""
# 总结：
# 1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
# 2、字符串可以用+运算符连接在一起，用*运算符重复。
# 3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
# 4、Python中的字符串不能改变。
