# Python3 中有六个标准的数据类型：
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Sets（集合）
# Dictionary（字典）

# 此处说明Tuple
# 元组（tuple）与列表List类似，不同之处在于元组的元素不能修改，元组写在小括号 () 里，元素之间用逗号","隔开,元组中的元素类型也可以不相同：
# 如一下实例:
tuple = ('ABC', 32, 12.23, '你好Python')
subtuple = ('subtuple', 8881, 88.11, "嘿嘿")
# 输出完整元组
print(tuple)  # ('ABC', 32, 12.23, '你好Python')

# 输出元组的第一个元素
print(tuple[0])  # ABC

# 输出元组的逆序的第一个元素
print(tuple[-1])  # 你好Python

# 输出从第二个元素开始到第三个元素
print(tuple[1:3])  # (32, 12.23)

# 输出从第二个元素开始的所有元素
print(tuple[1:])  # (32, 12.23, '你好Python')
# 输出两次元组
print(subtuple * 2)  # ('subtuple', 8881, 88.11, '嘿嘿', 'subtuple', 8881, 88.11, '嘿嘿')
# 连接元组
result = tuple + subtuple
print(result)  # ('ABC', 32, 12.23, '你好Python', 'subtuple', 8881, 88.11, '嘿嘿')


#元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取,其实，可以把字符串看作一种特殊的元组。
#tuple[0]="2323"
#print(subtuple)
#元组元素是不允许被修改的，因此这里将抛出 TypeError: 'tuple' object does not support item assignment异常


#虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
#构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 = ()    # 空元组
print(tup1)
tup2 = (20,) # 一个元素，需要在元素后添加逗号
print(tup2)#添加逗号打印的结果是：(20,) 不添加逗号的结果是:20


#string、list和tuple都属于sequence（序列）。
#总结：
#1、与字符串一样，元组的元素不能修改。
#2、元组也可以被索引和切片，方法一样。
#3、注意构造包含0或1个元素的元组的特殊语法规则。
#4、元组也可以使用+操作符进行拼接。








