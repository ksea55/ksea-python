# Python3 中有六个标准的数据类型：
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Sets（集合）
# Dictionary（字典）

# 此处说明Number


# Number（数字），Python3 支持 int、float、bool、complex（复数）。
# 在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# 像大多数语言一样，数值类型的赋值和计算都是很直观的。
# 内置的 type() 函数可以用来查询变量所指的对象类型。


a, b, c, d = 1, 100.22, True, 1 + 2j
print(a, b, c, d)  # 打印结果:1 100.22 True (1+2j)

print("a:" + str(type(a)) + ",b:" + str(type(b)) + ",c:" + str(type(c)) + ",d:" + str(type(d)))
# 打印结果：a:<class 'int'>,b:<class 'float'>,c:<class 'bool'>,d:<class 'complex'>

# 此外还可以用 isinstance 来判断：

result = isinstance(a, int)
print(result)  # 打印结果:True 表示 a是int类型


# isinstance 和 type 的区别在于：

# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
# 注意：在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。

# 如一下案例:
class A:  # 父类
    pass


class B(A):  # B类继承了A类
    pass


print("type(A())==A结果是:" + str(type(A()) == A))  # type(A())==A结果是:True
print("isinstance(A(),A)结果是:" + str(isinstance(A(), A)))  # isinstance(A(),A)结果是:True

print("type(B())==A结果是:" + str(type(B()) == A))  # type(B())==A结果是:False
print("isinstance(B(),A)结果是:" + str(isinstance(B(), A)))  # isinstance(B(),A)结果是:True

# 数值运算

# 加法
print(5 + 4)  # 结果：9
# 减法
print(4.3 - 2)  # 结果：2.3
# 乘法
print(3 * 7)  # 结果：21
# 乘方
print(2 ** 5)  # 结果：32
# 除法，得到一个浮点数
print(2 / 4)  # 结果：0.5
# 除法，得到一个整数
print(2 // 4)  # 结果：0
# 取余
print(17 % 3)  # 结果：2
