# Python3 中有六个标准的数据类型：
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Sets（集合）
# Dictionary（字典）

# 此处说明List
# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
# 列表是写在方括号([])之间、用逗号分隔开的元素列表。
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
# 列表截取的语法格式如下：
# 变量[头下标:尾下标]
# 索引值以 0 为开始值表示以正向开始，-1 为从末尾的开始位置 表示逆向开始。
# 加号（+）是列表连接运算符，星号（*）是重复操作。如下实例：

mylist = ['A', 12, 12.11, True, 'Complex', '你好Python']  # 创建一个list集合

print(mylist)  # 打印结果:['A', 12, 12.11, True, 'Complex', '你好Python']
print(mylist[0])  # 打印结果:A 截取第一个元素
print(mylist[-1])  # 打印结果：你好Python  截取逆向顺序第一个元素
print(mylist[0:])  # 打印结果：['A', 12, 12.11, True, 'Complex', '你好Python']  截取从0开始的所有数据
print(mylist[0:2])  # 打印结果：['A', 12] 截取下标索引在0-2之间的元素，但不包含下标索引2的元素

# * 表示重复操作当前集合mylist元素  2表示重复操作mylist元素的次数
print(mylist * 2)  #:打印结果：['A', 12, 12.11, True, 'Complex', '你好Python', 'A', 12, 12.11, True, 'Complex', '你好Python']

sublist = ["B", 333, 44.11, False, "嘿嘿"]

resultList = mylist + sublist;
print("mylist的长度:" + str(mylist.__len__()) + ",subList的长度：" + str(sublist.__len__()) + ",resultList的长度:" + str(
    resultList.__len__()) + ",resultList的元素:" + str(resultList))
# 打印结果:mylist的长度:6,subList的长度：5,resultList的长度:11,resultList的元素:['A', 12, 12.11, True, 'Complex', '你好Python', 'B', 333, 44.11, False, '嘿嘿']


# list与string不一样，list是可以改变集合中的元素的值的：

t = ['A', 12, 12.11, True, 'Complex', '你好Python']

a=t[0:2]
print(str(a))#['A', 12]

t[0]='ABC'
print(t) #['ABC', 12, 12.11, True, 'Complex', '你好Python'] 值已经发生改变

t[0:2]=[]
print(t) # [12.11, True, 'Complex', '你好Python'] 此处相当于删除了0，2之间的元素

t[0:2]=["E","F","G"]
print(t) #['E', 'F', 'G', 'Complex', '你好Python']


#总结：
#1、List写在方括号之间，元素用逗号隔开。
#2、和字符串一样，list可以被索引和切片。
#3、List可以使用+操作符进行拼接。
#4、List中的元素是可以改变的。