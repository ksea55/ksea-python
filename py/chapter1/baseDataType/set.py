# Python3 中有六个标准的数据类型：
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Sets（集合）
# Dictionary（字典）

# 此处说明Sets

# 集合（set）是一个无序不重复元素的序列。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典

# 创建一个sets集合字典
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# 输出集合，重复的元素被自动去掉
print(student)  # 打印结果:{'Rose', 'Mary', 'Jim', 'Jack', 'Tom'} sets是无序的因此每次打印结果的顺序都不一样

if "Rose" in student:
    print("Rose在students集合中..")
else:
    print("Rose不在students集合中..")
# 打印结果:Rose在students集合中..

# 创建一个空集合
a1 = set()
print(a1)  # 打印结果:set()

# set可以进行集合运算
a = set('abracadabra')
print(a)  # 打印结果:{'d', 'b', 'c', 'a', 'r'} 因为sets集合是无序无重复数据，自动去重
b = set('alacazam')
print(b)  # 打印结果{'m', 'z', 'l', 'a', 'c'} 因为sets集合是无序无重复数据，自动去重

# a和b的差集
print(a - b)  # 打印结果:{'r', 'b', 'd'}
# a和b的并集
print(a | b)  # 打印结果:{'m', 'c', 'a', 'r', 'd', 'b', 'l', 'z'}
# a和b的交集
print(a & b)  # 打印结果:{'a', 'c'}
# a和b中不同时存在的元素
print(a ^ b)  # 打印结果:{'d', 'r', 'z', 'l', 'b', 'm'}
