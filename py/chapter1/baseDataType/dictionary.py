# Python3 中有六个标准的数据类型：
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Sets（集合）
# Dictionary（字典）

# 此处说明Dictionary

# Dictionary（字典）字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。键(key)必须使用不可变类型。 在同一个字典中，键(key)必须是唯一的。



# 用{}定义一个字典数据类型
dic = {}
print(dic)  # 打印结果:{}

dic['one'] = "hello Python"  # 这里的one是字典类型的key 后面是它的value
dic[1] = "你好 python"  # 这里的1是字典类型的key 后面是它的value

# 这里我们可以把字典类型理解为javascript的json对象
print(dic['one'])  # hello Python
print(dic[1])  # 你好 python

# 当key重复的情况
dic[1] = "hi python";
print(dic[1])  # 当key一样的时候，后面的key的value会覆盖前面的value这个就跟java的map是一样的

# 定义一个字典类型数据，这个就是完全是json对象
tinydict = {'name': 'jacky', 'no': 1, 'site': 'www.jacky.com'}
# 打印字典类型
print(tinydict)  # {'name': 'jacky', 'no': 1, 'site': 'www.jacky.com'}

# 获取字典数据的所有key键值，这个完全与java的map操作一致
keys = tinydict.keys();
print(keys)  # dict_keys(['name', 'no', 'site'])

# 遍历key
for k in keys:
    print(k)
# 此处将keys转换成list数据类型 再取元素的第一个值
print(list(keys)[0])  # name

# 获取字典数据的所有values的值
values = tinydict.values();
print(values)  # dict_values(['jacky', 1, 'www.jacky.com'])

# 遍历所有的values
for v in values:
    print(v)

print(list(values)[0])  # jacky

# 字典数据类型的构造函数 dict(),此处利用dict()构造函数构造一个字典数据类型
dic = dict([("taobao.com", "mayun"), ("baidu.com", "lyh"), ("36.com", "jiaozhu")])
print(dic)  # 打印结果:{'taobao.com': 'mayun', 'baidu.com': 'lyh', '36.com': 'jiaozhu'}

print(dic["taobao.com"])  # mayun
print(dic.keys())  # dict_keys(['taobao.com', 'baidu.com', '36.com'])
print(dic.values())  # dict_values(['mayun', 'lyh', 'jiaozhu'])

#注意：
#1、字典是一种映射类型，它的元素是键值对。
#2、字典的关键字必须为不可变类型，且不能重复。
#3、创建空字典使用 { }。
