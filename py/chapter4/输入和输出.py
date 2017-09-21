# 输入和输出
# 在前面几个章节中，我们其实已经接触了 Python 的输入输出的功能。本章节我们将具体介绍 Python 的输入输出。
# 输出格式美化
# Python两种输出值的方式: 表达式语句和 print() 函数。
# 第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
# 如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
# 如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。


s1 = "Hello,world!"
print(str(s1))  # Hello,world!
print(repr(s1))  # 'Hello,world!'

s2 = "hello \n  python!"
print(s2)
# hello
# python!
print(str(s2))
# hello
# python!

#  repr() 函数可以转义字符串中的特殊字符
print(repr(s2))  # 'hello \n  python!'
# 等同于
print(str(r"hello  \n python!"))  # hello  \n python!

# repr() 的参数可以是 Python 的任何对象
s3 = repr((12, 12.2, True, ["python", "Java"], ("red", "blue"), set("ABCD"), {"name": "ksea", "age": 21}))
print(s3)  # (12, 12.2, True, ['python', 'Java'], ('red', 'blue'), {'B', 'C', 'D', 'A'}, {'name': 'ksea', 'age': 21})

# 这里有两种方式输出一个平方与立方的表

for x in range(1, 4):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end="")
    print(repr(x * x * x).rjust(4))
"""
打印结果:
 1   1   1
 2   4   8
 3   9  27

"""

# 这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
# 还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
# 另一个方法 zfill(), 它会在数字的左边填充 0，如下所示：


print("12".zfill(5))  # 00012
print('-3.14'.zfill(7))  # '-003.14'
print('3.14159265359'.zfill(5))  # '3.14159265359'

# str.format() 的基本使用如下:


# 括号{} 及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))  # 菜鸟教程网址： "www.runoob.com!"

# 在括号中的数字用于指向传入对象在 format() 中的位置，如下所示：
print('{0} 和 {1}'.format('Google', 'Runoob'))  # Google 和 Runoob
print('{1} 和 {0}'.format('Google', 'Runoob'))  # Runoob 和 Google

# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))  # 菜鸟教程网址： www.runoob.com  # 位置及关键字参数可以任意的结合:\

print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))  # 站点列表 Google, Runoob, 和 Taobao。

# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
import math

print('常量 PI 的值近似为： {}。'.format(math.pi))  # 常量 PI 的值近似为： 3.141592653589793。
print('常量 PI 的值近似为： {!r}。'.format(math.pi))  # 常量 PI 的值近似为： 3.141592653589793。

# 可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：

print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))  # 常量 PI 的值近似为 3.142。
print('常量 PI 的值近似为 {name:.3f}。'.format(name=math.pi))  # 常量 PI 的值近似为 3.142。

print("--------------------------------------------------------------------")
print('常量 PI 的值近似为 {0:.3f}'.format(math.pi))  # 常量 PI 的值近似为 3.142
"""
解释:
{0:.3f} 其中0表示参数的占位符，表示在format中的第一个参数
{name:.3f} 它与上面一样 只不过这里是用的命名的方式来替代占位符
{0:.3f} 表示对其结果数据在小数点.后面保留三位小数
"""

# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10}==>{1:10d}'.format(name, number))
"""
打印结果:
Google    ==>         1
Runoob    ==>         2
Taobao    ==>         3
"""

# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
# 最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值 :
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
# Runoob: 2; Google: 1; Taobao: 3

# 也可以通过在 table 变量前使用 '**' 来实现相同的功能：这个就相当于用命名的参数方式，key作为参数命名的占位符
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
# Runoob: 2; Google: 1; Taobao: 3
