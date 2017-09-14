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
