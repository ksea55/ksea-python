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
