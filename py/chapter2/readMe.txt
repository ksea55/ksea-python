主要讲解 基本数据类型的使用方法和函数
Number

# Python3 数字(Number)
# Python 数字数据类型用于存储数值。
# 数据类型是不允许改变的,这就意味着如果改变数字数据类型得值，将重新分配内存空间。
# 以下实例在变量赋值时 Number 对象将被创建：
var1 = 1
var2 = 10
# 此刻就被分配了2个内存空间

print(var1 is var2)  # 打印结果:False 其中is主要用于比较其内存地址是否一样  ==主要比较2个值是否相等
var3 = 1
print(var1 is var3)  # 打印结果:True 可以看见 数据类型的数字一样 其内存映射的地址也是一样的

# del 删除一些数字对象的引用。
# del语句的语法是：
# del var1[,var2[,var3[....,varN]]]]

# del  var1
# print(var1) 当运行时，这里就会抛出 NameError: name 'var1' is not defined 异常 表示var1变量已经被删除，进而是未声明的变量




# Python 支持三种不同的数值类型：

# 整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。
# 浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
# 复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。




# Python 数字类型转换

# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
# int(x) 将x转换为一个整数。
# float(x) 将x转换到一个浮点数。
# complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
# complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式


# 这里说明几个比较常用的函数，开发中运用到其它的在查询就是了


n1 = 10.5
n2 = 11.5

# 向下取舍
import math

print(math.floor(n1))  # 打印结果:10
print(math.floor(n2))  # 打印结果:11

n3 = 11.4
# 向上取舍
print(round(n1))  # 打印结果：10
print(round(n2))  # 打印结果：12
print(round(n3))  # 打印结果：11
# 注意round()四舍五入取舍的规则，对偶数是向下取舍相当于math.floor(),对于奇数是向上四舍五入取舍

n4 = 11.0233
print(round(n4, 2))  # 打印结果：11.02 round()函数中的第二个参数表示保留多少位小数

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
import random

random.shuffle(list1)  # shuffle将对列表元素进行随机排序
print(list1)  # [9, 7, 6, 8, 5, 2, 1, 3, 4]



#生成随机数字
r=random.random()
print(r) #0.8838579176025544






String

# Python中提供了非常强大format格式化


# 字符串格式化   在python中是使用{}来充当其占位符
s1 = "hello {}".format("python")
print(s1)  # 打印结果:hello python

s2 = "{},{},{}".format("你好", "python", "nice")
print(s2)  # 打印结果:你好,python,nice 可以看出在format中的参数是依次替代{}的，其中format的参数值必须与{}个数保持一致或者会报错

s3 = "{1},{0},{2}".format("python", "hello", "你最棒!")
print(s3)  # 打印结果:hello,python,你最棒! 其中{1},{0},{2} 数字代表format的参数的位置

s4 = "大家好我叫{name},今年{age}岁".format(name="ksea", age=21)
print(s4)  # 打印结果：大家好我叫ksea,今年21岁 使用其命名参数的方式

list1 = ["jacky", 21]
s5 = "大家好我叫{0[0]},今年{0[1]}岁".format(list1)
print(s5)  # 打印结果:大家好我叫jacky,今年21岁 通过列表下标，不过这里的注意是{0}加上下标{0[下标值]}

s6 = '{:.2f}'.format(321.33345)
print(s6)  # 打印结果:321.33
# 其中.2表示长度为2的精度，f表示float类型。 注意这里是用的:


s7 = "{:,}".format(1234565677)
print(s7)  # 打印结果:1,234,565,677  用逗号自动隔离其千位分割

s8 = "{:,.2f}".format(1234565677)
print(s8)  # 打印结果:1,234,565,677.00  用逗号自动分割千位，并保留2位精度

# 将字符串的第一个字符转换为大写 函数capitalize()
print("hello".capitalize())  # 打印结果:Hello

print("--------------------------------------------------------------------------")



# 函数：count(str, beg= 0,end=len(string)) 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
s9 = "dfdjlajlgdfdahfkjdg";
print("出现d的次数:", s9.count('d'))  # 打印结果:5
print("指定区间出现出现d的次数:", s9.count('d', 1, 4))  # 打印结果：1
print("------------------------------------------------------------------------------------")



# encode(encoding='UTF-8',errors='strict') 以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
s10 = str.encode('你好', 'GBK', '编码错误')
print(s10)  # 打印结果:b'\xc4\xe3\xba\xc3'

# bytes.decode(encoding="utf-8", errors="strict") Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
s11 = bytes.decode(s10, "GBK", "解码错误")
print(s11)  # 打印结果:你好
print("------------------------------------------------------------------------------------")





# endswith(suffix, beg=0, end=len(string))检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
print("abcd".endswith("cd"))  # 打印结果:True
print("abcdafdd".endswith("cd", 0, 4))  # 此处包含范围检索,实际检索的是abcd的范围 打印结果：True

# startswith(str, beg=0,end=len(string)) 检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
print("abcd".startswith("ab"))  # 打印结果:True
print("abcdafdd".endswith("ab", 0, 4))  # 此处包含范围检索,实际检索的是abcd的范围 打印结果：True

print("------------------------------------------------------------------------------------")



# expandtabs(tabsize=8) 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
s12 = "你好  python  !"
print(s12)  # 你好  python  ! 此处是用tab间隔
print(s12.expandtabs())  # 你好  python  ! 此处tab被转换成空格

print("------------------------------------------------------------------------------------")





# find(str, beg=0 end=len(string)) 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
# rfind(str, beg=0,end=len(string))与find()函数一样，不过它是从右边开始查找.
s13 = "abcd"
print(s13.find("c"))  # 打印结果:2 因为其下标是从0开始的 因此c返回的位置就是2
print(s13.find("h"))  # 打印结果:-1 没有找到就返回-1

# index(str, beg=0, end=len(string)) 跟find()方法一样，只不过如果str不在字符串中会报一个异常.
# rindex( str, beg=0, end=len(string))它与index()函数一样，不过是从右边开始.

print(s13.index("c"))  # 打印结果:2 因为其下标是从0开始的 因此c返回的位置就是2
# print(s13.index("h")) #用index检索某个字符串，其不存在的时候不是返回-1而是抛出异常 ValueError: substring not found 这个也是index与find的区别



print("------------------------------------------------------------------------------------")



# isalnum()如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
print("abc".isalnum())  # True
print("1234".isalnum())  # True
print("abc1234".isalnum())  # True
print("abc1234_".isalnum())  # False
# 总结 isalnum()函数 当其字符串只是字母或者数字就返回True或者就是False




# isalpha()如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False,它主要用于检索某个字符串中的字符是否全是[a-z A-Z]
print("abc".isalpha())  # True
print("ABC".isalpha())  # True
print("abcABC".isalpha())  # True
print("234".isalpha())  # False
print("abc234".isalpha())  # False

# isdigit() 如果字符串只包含数字则返回 True 否则返回 False.. 用于检索字符串是否是村纯数字字符串 [0-9]
print("0".isdigit())  # True
print("012".isdigit())  # True
print("323aA".isdigit())  # False
print("0.12".isdigit())  # False

# isnumeric()如果字符串中只包含数字字符，则返回 True，否则返回 False 其与isdigit()一样
print(".".isnumeric())  # False
print("0.2".isnumeric())  # False
print("12".isnumeric())  # True

# islower() 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False 言简意赅判定某个字母字符串是否是全小写
print("ABC".islower())  # False
print("abc".islower())  # True
print("ABCabc".islower())  # False
print("122".islower())  # False

# isupper() 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False 言简意赅判定某个字母字符串是否是全大写

print("ABC".islower())  # True
print("abc".islower())  # False
print("ABCabc".islower())  # False
print("122".islower())  # False

# isspace()如果字符串中只包含空白，则返回 True，否则返回 False.
print("".isspace())  # False
print(" ".isspace())  # True

# istitle()如果字符串是标题化的(见 title())则返回 True，否则返回 False 标题化也就是在单词中 首字母是大写 其余是小写，可以通过函数title()来进行标题化转换
print("dfd".istitle())  # False
print("python主题".istitle())  # False
print("Title".istitle())  # True
s14 = "title"
print(s14.title())  # Title





# join(seq) 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
s15 = ["A", "B", "C", "D"]
p1 = "-"  # 分隔符 -
p2 = ""  # 以空格作为分隔符
print(p1.join(s15))  # A-B-C-D 以分隔符- 将列表中的数据连接起来 合并成一个新的字符串
print(p2.join(s15))  # ABCD 以空格分隔符，将列表中的数据连接起来，合并成一个新的字符串
print("------------------------------------------------------------------------------------")




# len(string)返回字符串长度
s16 = "abcd"
print(len(s16))  # 打印结果:4 字符串长度为：4

print("------------------------------------------------------------------------------------")




# lower()转换字符串中所有大写字符为小写.
print("ABCD".lower())  # abcd

# upper()转换字符串中的小写字母为大写
print("abcd".upper())  # ABCD

# swapcase() 将字符串中大写转换为小写，小写转换为大写
print("ABCDefgafABC".swapcase())  # 打印结果:abcdEFGAFabc

print("------------------------------------------------------------------------------------")





# lstrip()截掉字符串左边的空格或指定字符。
print("   abc dfd fdf  ".lstrip())  # abc dfd fdf
print("abchhh".lstrip("ab"))  # chhh
# rstrip()删除字符串字符串末尾的空格或指定字符。
print("   abc dfd fdf  ".rstrip())  # abc dfd fdf
print("abcdef".rstrip("ef"))  # abcd

# strip([chars]) 在字符串上执行 lstrip()和 rstrip() 也就是去掉前后的空格
print("  Hello  Python ! I Love You    ".strip())  # Hello  Python ! I Love You

print("------------------------------------------------------------------------------------")

s17 = "abcdABCD"
# max(str)返回字符串 str 中最大的字母。
print(max(s17))  # d
# min(str)返回字符串 str 中最小的字母。
print(min(s17))  # A
print("------------------------------------------------------------------------------------")

# maketrans()创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# 其中：两个字符串的长度必须相同，为一一对应的关系。
# 注：Python3.4已经没有string.maketrans()了，取而代之的是内建函数: bytearray.maketrans()、bytes.maketrans()、str.maketrans()
# 语法
# maketrans()方法语法：
# str.maketrans(intab, outtab)
# 参数
# intab -- 字符串中要替代的字符组成的字符串。
# outtab -- 相应的映射字符的字符串。
# 返回值
# 返回字符串转换后生成的新字符串。
# 实例
# 以下实例展示了使用maketrans() 方法将所有元音字母转换为指定的数字：
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
# 此处trantab 是字符映射之后的转换表 其中a对应1 额对应2 i对应3 o对应4 u对应5

# translate(table, deletechars="")根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
str = "this is string example....wow!!!"
print(str.translate(trantab))  # 打印结果:th3s 3s str3ng 2x1mpl2....w4w!!! 根据trantab的转换表 将对应的字母转换成对应的数字

print("------------------------------------------------------------------------------------")

# replace(old, new [, max])把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
s18 = "aello python !"
print(s18.replace("a", "h"))  # hello python !
print("abc aec adc ahc".replace("a", "A", 2))  # Abc Aec adc ahc 被限定最多只能替换两次

print("------------------------------------------------------------------------------------")




# ljust(width,[, fillchar]) 返回一个原字符串左对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
# rjust(width,[, fillchar]) 返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串

# 语法 上面两个语法一样
# rjust()方法语法：
# str.rjust(width[, fillchar])
# 参数
# width -- 指定填充指定字符后中字符串的总长度.
# fillchar -- 填充的字符，默认为空格。

# 例如一下案例，数字长度5 按左对齐 不够位数用0填充
print("123".ljust(5, "*"))  # 打印结果:123**  表示按左对齐，其对其长度为5 当长度不够是用*字符进行填充
print("123".rjust(5, "?"))  # 打印结果:??123   表示按右对齐，其对其长度为5 当长度不够是用?字符进行填充

print("------------------------------------------------------------------------------------")

# split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
# 语法 str.split(str="", num=string.count(str))
# 参数
# str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# num -- 分割次数。

str = "this is string example....wow!!!"
print(str.split())  # 以空格进行分割，并返回其分割后的列表  打印结果:['this', 'is', 'string', 'example....wow!!!']
print(str.split('is', 1))  # 以is分割符进行分割并且按照分隔符is只分割指定次数 1 次 打印结果: ['th', ' is string example....wow!!!']
print(str.split('w'))  # 以 w 分隔符进行分割 打印结果:['this is string example....', 'o', '!!!']

# splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
# 语法：str.splitlines([keepends])
# 参数
# keepends -- 在输出结果里是否去掉换行符('\r', '\r\n', \n')，默认为 False，不包含换行符，如果为 True，则保留换行符。

print('ab c\n\nde fg\rkl\r\n'.splitlines())  # 打印结果:    ['ab c', '', 'de fg', 'kl']
print('ab c\n\nde fg\rkl\r\n'.splitlines(True))  # 打印结果:    ['ab c\n', '\n', 'de fg\r', 'kl\r\n']

print("------------------------------------------------------------------------------------")

# zfill (width) 返回长度为 width 的字符串，原字符串右对齐，前面填充0

print("abcddf".zfill(12))  # 打印结果:000000abcddf

# isdecimal() 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。

print("1212".isdecimal())  # True
print("12.22".isdecimal())  # False
print("0".isdecimal())  # Trule
print("abc".isdecimal())  # False

print("------------------------------------------------------------------------------------")







List



# 序列(List)是Python中最基本的数据结构,可以理解成java中的数组，向它一样分配，取值
# Python有6个序列的内置类型，但最常见的是列表和元组。
# 序列都可以进行的操作包括索引，切片，加，乘，检查成员。
# 此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
# 列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
# 列表的数据项不需要具有相同的类型
# 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：

print("---------------------------------------------------------------------------------------------------------------")

list1 = ['Google', 'Baidu', 1997, 2000, 12.22, True];
list2 = [1, 2, 3, 4, 5];

print("list1[0]: ", list1[0])  # list1[0]:  Google
# print("list1[11]: ",list1[11]) # 当根据索引获取列表的值，其超出列表长度会抛出异常：IndexError: list index out of range
print("list2[1:5]: ", list2[1:7])  # list2[1:5]:  [2, 3, 4, 5] 有意思的是在python中 截取的长度超过其本身长度而不会报错

# 更改list数据
print("更新前list1[0]:", list1[0])  # 更新前list1[0]: Google
list1[0] = "Taobao"
print("更新后list1[0]:", list1[0])  # 更新后list1[0]: Taobao

# 删除list列表中的元素的引用

del list1[0]
print("使用del删除之后的list1的结果:", list1)  # 使用del删除之后的list1的结果: ['Baidu', 1997, 2000, 12.22, True]

print("---------------------------------------------------------------------------------------------------------------")

# Python列表脚本操作符

L1 = [1, 2, 3]
L2 = [4, 5]
S1 = L1 + L2  # [1, 2, 3, 4, 5] 列表用+号连接,会将两个列表中的元素合并成一个列表并返回
print(S1)

S2 = L2 * 3
print(S2)  # [4, 5, 4, 5, 4, 5]  * 表示重复该列表中的元素，3表示重复该列表中的元素多少次，然后将这些元素重新组合成一个新的列表并返回

S3 = 2 in L1
print(S3)  # True in 表示 in前面的元素是否存在in后面的列表中，如果该元素存在则返回True 否则就返回False

for x in L1:
    print(x, end="")  # 迭代列表，并不换行 用空格符号进行连接

# 列表中的元素截取与字符串中的截取方法一样

# 列表中的列表嵌套列表操作

S4 = [L1, L2]
print(S4)  # 打印结果：[[1, 2, 3], [4, 5]]

S5 = S4[0]
print(S5)  # 打印结果:[1, 2, 3]

S6 = S5[1]
print(S6)  # 打印结果:2

S7 = S4[0][1]
print(S7)  # 打印结果:2 这个就相当于java中的二维数组一样

print("---------------------------------------------------------------------------------------------------------------")

# Python列表中的函数&方法

# len(list)获取列表元素个数的长度 相当于java中的size()
L3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(L3))  # 打印结果:9
print(L3.__len__())  # 打印结果：9

# max(list) 返回列表元素最大值
print(max(L3))  # 打印结果：9

# min(list) 返回列表元素最小值
print(min(L3))  # 打印结果：1

# list(seq) 将元组转换为列表
y1 = (12344, "Tuple", 23.22, True, "python")  # 注意元祖 在创建的时候如果元组只有一个元素后面需要添加,如：y1=(1221,)不添加会报错
L4 = list(y1)
print(L4)  # [12344, 'Tuple', 23.22, True, 'python']

print("---------------------------------------------------------------------------------------------------------------")

#	list.append(obj) 在列表末尾添加新的对象

L5 = ["A", 12, 14.11, True]
L5.append("Python")
print(L5)  # 打印结果:['A', 12, 14.11, True, 'Python']

#	list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

L6 = ["ABC", "DFC"]
L7 = [12, 44.11, False]
L6.extend(L7)
print(L6)  # 打印结果:['ABC', 'DFC', 12, 44.11, False]

#	list.count(obj) 统计某个元素在列表中出现的次数

L8 = ["A", "BC", "ABC", "A", "ADF"]
print(L8.count("A"))  # 打印结果:2

#	list.index(obj) 从列表中找出某个值第一个匹配项的索引位置

print(L8.index("A"))  # 打印结果：0
# print(L8.index("B"))  # 当查找的值不在列表中会抛出异常--> ValueError: 'B' is not in list


#	list.insert(index, obj) 将对象插入列表

L9 = ["ABC", "DFG"]
L9.insert(1, "python")
print(L9)  # ['ABC', 'python', 'DFG'] #将对象插到指定位置，如果该位置元素已经存在，将会向后移位
L9.insert(6, "Hello python")
print(L9)  # ['ABC', 'python', 'DFG', 'Hello python'] #当插入的元素 所在的索引超过列表长度 默认会将该元素插入到元素最后

#	list.pop(obj=list[-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

L10 = ["A", "B", "C", "D", "E", "F"]
V1 = L10.pop()
print(V1, "--", L10)  # 打印结果:F -- ['A', 'B', 'C', 'D', 'E']  pop()方法跟java的linkedList的方法一样

V2 = L10.pop(2)  # 移除指定位置的元素
print(V2, "--", L10)  # 打印结果:C -- ['A', 'B', 'D', 'E']

#	list.remove(obj) 移除列表中某个值的第一个匹配项

L11 = ["A", "B", "A", "D", "A", "F"]
L11.remove("A")  # 这里将把首先匹配到的元素进行删除，然后就返回列表，而不会继续往后移除，可以这样理解，遍历某个集合，当找到这个匹配的元素删除，立马break;
print(L11)

#	list.reverse() 反向列表中元素

L12 = ["A", "B", "C", "D", "E", "F"]
L12.reverse()
print(L12)  # ['F', 'E', 'D', 'C', 'B', 'A']

#	list.sort([func]) 对原列表进行排序

L13 = [3, 1, 6, 2, 8, 1]
L13.sort()
print(L13)  # [1, 1, 2, 3, 6, 8]
L13.sort()

#	list.clear() 清空列表

L13.clear()
print(L13)  # 打印结果:[]
print(len(L13))  # 打印结果：0

#	list.copy() 复制列表

L14 = ["A", "B", "C"]
L15 = L14.copy()
print(L15)  # ['A', 'B', 'C']

print("---------------------------------------------------------------------------------------------------------------")




Tuple



# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号()，列表使用方括号[]。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

# 创建一个有数据的元组
t1 = (12, 11.01, "Python", True)

# 定义一个空元组
t2 = ()
print(t2)

# 当元组元素中只有一个元素，需要添加其逗号

t3 = ("A")  # 没加逗号,的情况，其结果是，元素是什么类型就是什么类型，而不是元组类型
print(type(t3))  # 打印结果:<class 'str'>

t4 = ("A",)  # 一个元素加了逗号,就是元组类型
print(type(t4))  # 打印结果:<class 'tuple'>

# 元组的取值与String一样
t5 = ('Google', 'Taobao', 1997, 2000.1, True)
t6 = (1, 2, 3, 4, 5, 6, 7)

print("t5[0]: ", t5[0])  # t5[0]:  Google
print("tup6[1:5]: ", t6[1:5])  # tup6[1:5]:  (2, 3, 4, 5)

# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合

t7 = ("A", "B", "C")
t8 = ("X", "Y", "Z")

# t7[0] = "P";  # 此处抛出异常，表示元组元素不允许更改： TypeError: 'tuple' object does not support item assignment
print(t7)

t9 = t7 + t8
print(t9)  # ('A', 'B', 'C', 'X', 'Y', 'Z')

# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:

tup = ('Google', 'Taobao', 1997, 2000)
print(tup)

# del tup[0]  #TypeError: 'tuple' object doesn't support item deletion
print("删除后的元组 tup : ")
del tup
# print(tup)  # NameError: name 'tup' is not defined 此处表示tup已经被删除




# 元组运算符
# 与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。

# 计算元素个数
l = len((1, 2, 3))
print(l)  # 3
#		连接
l1 = (1, 2, 3) + (4, 5, 6)
print(l1)  # (1, 2, 3, 4, 5, 6)
l2 = ('Hi!',) * 4
print(l2)  # ('Hi!', 'Hi!', 'Hi!', 'Hi!')
# 元素是否存在
l3 = 3 in (1, 2, 3)
print(l3)  # True
for x in (1, 2, 3):
    print(x)  # 1 2 3	迭代

print("-----------------------------------------------------------------")

# max(tuple) 返回元组中元素最大值。
tuple2 = ('5', '4', '8')
print(max(tuple2))  # 8

#	min(tuple) 返回元组中元素最小值。
print(min(tuple2))  # 4
# tuple(seq) 将列表转换为元组。
list1 = ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1 = tuple(list1)
print(tuple1)  # ('Google', 'Taobao', 'Runoob', 'Baidu')



Dictionary

# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
# d = {key1 : value1, key2 : value2 }
# 键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
# 我们简单的可以把python中的dictionary理解成javascript的json即可
# 一个简单的字典实例：
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# 也可如此创建字典：
dict1 = {'abc': 456};
dict2 = {'abc': 123, 98.6: 37};

# 访问字典里的值，通过key获取value，这个就相当于java中的map一样如下实例:

dict3 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("dict['Name']: ", dict3['Name'])  # dict['Name']:  Runoob
print("dict['Age']: ", dict3['Age'])  # dict['Age']:  7

# 如果用字典里没有的键访问数据，会输出错误如下：
# print("dict['Alice']: ", dict3['Alice'])  # Traceback (most recent call last):  KeyError: 'Alice' 表示当前key不存在


# 字典的增，删，改

dict4 = {"name": "mexican", "age": 21}
print(dict4)  # {'name': 'mexican', 'age': 21}

# 获取name
name = dict4["name"]
print("name:", name)

# 修改name
dict4["name"] = "jacky"
print(dict4)  # {'name': 'jacky', 'age': 21}
print("name:", dict4["name"])  # name: jacky

# 向字典中添加元素
dict4["sex"] = "man"
print(dict4)  # {'name': 'jacky', 'age': 21, 'sex': 'man'}

# 对dictionary 进行删除操作

# 根据key删除某个值
del dict4["name"]
print(dict4)  # {'age': 21, 'sex': 'man'}

# 清空dictionary
dict4.clear()
print(dict4)  # {}

del dict4
# print(dict4)  # NameError: name 'dict4' is not defined,用del 删除某个变量的时候，这个变量就从栈中呗移除，此刻就没这个变量，因此访问的时候会抛出此异常



# Python字典包含了以下内置函数：

#	len(dict) 计算字典元素个数，即键的总数。
dict5 = {'Name': 'jacky', 'Age': 7, 'Class': 'First'}
print(len(dict5))  # 3

# str(dict) 输出字典，以可打印的字符串表示。
dstr5 = str(dict5)
print(dstr5)  # {'Name': 'jacky', 'Age': 7, 'Class': 'First'}

# type(variable) 返回输入的变量类型，如果变量是字典就返回字典类型。
dtype = type(dict5)
print(dtype)  # <class 'dict'>

# Python字典包含了以下内置方法：


dict6 = {'Name': 'jacky', 'Age': 7, 'Class': 'First'}

#	radiansdict.clear() 删除字典内所有元素
print(dict6)  # {'Name': 'jacky', 'Age': 7, 'Class': 'First'}
dict6.clear()
print(dict6)  # {}

#	radiansdict.copy() 返回一个字典的浅复制,在浅拷贝中，在拷贝中的数据修改，原始的数据也会修改

dict7 = {'Name': 'jacky', 'Age': 7, 'Class': 'First'}
d8 = dict7.copy()
d8["Name"] = "jacky"
print(dict7)  # {'Name': 'jacky', 'Age': 7, 'Class': 'First'}
print(d8)  # {'Name': 'jacky', 'Age': 7, 'Class': 'First'}

#	radiansdict.fromkeys() 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# 语法
# fromkeys()方法语法：
# dict.fromkeys(seq[, value]))
# 参数
# seq -- 字典键值列表。
# value -- 可选参数, 设置键序列（seq）的值。

listseq = ["name", "age", "email"]

dict8 = dict.fromkeys(listseq)  # 此处用listseq中的值来作为dict8的key，其值默认就是None 空值
print(dict8)  # {'name': None, 'age': None, 'email': None}

dict9 = dict.fromkeys(listseq, 10)  # 这里是同时设置了key与value，并且value的值都是10
print(dict9)  # {'name': 10, 'age': 10, 'email': 10}

#	radiansdict.get(key, default=None)返回指定键的值，如果值不在字典中返回default值

dict10 = {'Name': 'jacky', 'Age': 7, 'Class': 'First'}
d10 = dict10.get("Name")  # 根据key获取value与java中的map一样
print(d10)  # jacky
d11 = dict10.get("Name_")
print(d11)  # None 当key不存在，获取到的value的值是None,也就是default默认的值

#	key in dict 如果键在字典dict里返回true，否则返回false

dict11 = {'Name': 'jacky', 'Age': 7, 'Class': 'First'}
d12 = "Name" in dict11
print(d12)  # True
d13 = "Name_" in dict11
print(d13)  # False

#	radiansdict.items() 以列表返回可遍历的(键, 值) 元组数组

dict12 = {'Name': 'jacky', 'Age': 7, 'Class': 'First'}
tuple12 = dict12.items()  # 此时返回的是元组数据
print(tuple12)  # dict_items([('Name', 'jacky'), ('Age', 7), ('Class', 'First')])

# 遍历该元组数据
for key, val in tuple12:
    print(key, ":", val, end="   ")  # 打印结果：Name : jacky   Age : 7   Class : First

# radiansdict.keys() 以列表返回一个字典所有的键

dict12 = {'Name': 'jacky', 'Age': 7, 'Class': 'First'}
keys = dict12.keys()  # 返回的也是一个元组
print(keys)  # dict_keys(['Name', 'Age', 'Class'])
for k in keys:
    print(k)

# radiansdict.values() 以列表返回字典中的所有值

dict13 = {'Name': 'jacky', 'Age': 7, 'Class': 'First'}
values = dict13.values()
print(values)  # dict_values(['jacky', 7, 'First'])
val_list = list(values)  # ['jacky', 7, 'First']
print(val_list, "-", val_list[0])  # ['jacky', 7, 'First'] - jacky

#	radiansdict.setdefault(key, default=None) 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default

dict14 = {'Name': 'jacky', 'Age': 7, 'Class': 'First'}
dict14.setdefault("email", "default.com")  # 对其字典设置默认值，如果该key不存在，其值就是default.com
print(dict14)  # {'Name': 'jacky', 'Age': 7, 'Class': 'First', 'email': 'default.com'}
dict14["email"] = "jacky@126.com"  # 添加字典数据
print(dict14)  # {'Name': 'jacky', 'Age': 7, 'Class': 'First', 'email': 'jacky@126.com'}

del dict14["email"]
print(dict14)  # {'Name': 'jacky', 'Age': 7, 'Class': 'First'}

#	pop(key[,default]) 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。

dict15 = {'Name': 'jacky', 'Age': 7, 'Class': 'First'}
val15 = dict15.pop("Name")  # 删除指定的key，并返回该key对应的value
print(val15)  # 打印结果:jacky

#	radiansdict.update(dict2) 把字典dict2的键/值对更新到dict里

dict16 = {'Name': 'jacky', 'Age': 7, 'Class': 'First'}
dict17 = {'Url': 'taobao.com', 'address': "成都"}

dict16.update(dict17)
print(dict16)  # {'Name': 'jacky', 'Age': 7, 'Class': 'First', 'Url': 'taobao.com', 'address': '成都'}

#	popitem() 随机返回并删除字典中的一对键和值(一般删除末尾对)。
dict18 = {'Name': 'jacky', 'Age': 7, 'Class': 'First'}
dic_18 = dict18.popitem()
print(dict18, "---", dic_18)  # {'Name': 'jacky', 'Age': 7} --- ('Class', 'First')
