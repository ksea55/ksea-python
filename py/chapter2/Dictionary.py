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
