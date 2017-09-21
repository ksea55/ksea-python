# 列表
# Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，一句话概括即：列表可以修改，而字符串和元组不能。

# 以下是 Python 中列表的方法：

# 方法	                描述

# list.append(x)  	    把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
# list.extend(L)	    通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
# list.insert(i, x)	    在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
# list.remove(x)	    删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
# list.pop([i])	        从列表的指定位置删除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被删除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
# list.clear()	        移除列表中的所有项，等于del a[:]。
# list.index(x)	        返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
# list.count(x)	        返回 x 在列表中出现的次数。
# list.sort()	        对列表中的元素进行排序。
# list.reverse()	    倒排列表中的元素。
# list.copy()	        返回列表的浅复制，等于a[:]。


list = ["D", "B", "A", "B", "D", "A", "E", "A", "H"]
print("countA:{A},countB:{B}".format(A=list.count("A"), B=list.count("B")))  # 统计A,B在list出现的次数  countA:3,countB:2

list.insert(-1, "X")
print(list)  # ['D', 'B', 'A', 'B', 'D', 'A', 'E', 'A', 'X', 'H']

list.append("Z")
print(list)  # ['D', 'B', 'A', 'B', 'D', 'A', 'E', 'A', 'X', 'H', 'Z']

index1 = list.index("A")
print("index1:", index1)  # index1: 2
try:
    index2 = list.index("Y")
    print("index2:", index2)  # 当要查找的数据不在list中会抛出--> ValueError: 'Y' is not in list
except ValueError:
    print("该元素在list中不存在")

list.remove("A")
print(list)  # ['D', 'B', 'B', 'D', 'A', 'E', 'A', 'X', 'H', 'Z'] #删除 第一个出现的A元素

try:
    list.remove("Y")
    print(list)  # 当删除一个不在list中的元素，会抛出异常-->ValueError: list.remove(x): x not in list
except ValueError:
    print("您所删除的元素不在list列表中!")

    # 打印结果:您所删除的元素不在list列表中!

list.reverse()
print(list)  # ['Z', 'H', 'X', 'A', 'E', 'A', 'D', 'B', 'B', 'D']

list.sort()
print(list)  # ['A', 'A', 'B', 'B', 'D', 'D', 'E', 'H', 'X', 'Z']

list1 = ["L", "M", "N"]
list1.extend(list)
print(list1)  # ['L', 'M', 'N', 'A', 'A', 'B', 'B', 'D', 'D', 'E', 'H', 'X', 'Z']

list1.pop(2)  # 删除指定位置2的元素
print(list1)  # ['L', 'M', 'A', 'A', 'B', 'B', 'D', 'D', 'E', 'H', 'X', 'Z']

list1.pop()  # 没有指定删除的位置 默认删除的是最后一个元素
print(list1)  # ['L', 'M', 'A', 'A', 'B', 'B', 'D', 'D', 'E', 'H', 'X']

list2 = list1.copy()  # 对其list1进行浅拷贝
print(list2)  # ['L', 'M', 'A', 'A', 'B', 'B', 'D', 'D', 'E', 'H', 'X']
# 修改浅拷贝列表
list2[0] = "K"
print(list2)  # ['K', 'M', 'A', 'A', 'B', 'B', 'D', 'D', 'E', 'H', 'X']
print(list1)  # ['L', 'M', 'A', 'A', 'B', 'B', 'D', 'D', 'E', 'H', 'X']

# python中将列表当做堆栈使用，主要运用其list特殊方法 append与pop
# 列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）。
# 用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。例如：

# 声明一个空列表
stack = []

stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")
print(stack)

s = stack.pop()  # 在没有指定元素位置的时候，默认是从元素末尾开始删除并返回
print(s)


# 自定义栈,此处主要用于模拟栈的数据结构
class MyStack:
    # 声明一个列表容器,对其进行初始化 self代表类的实例
    def __init__(self):
        self.data = []

    # 压栈
    def putStack(self, e):
        self.data.append(e)

    # 弹栈
    def pelletStack(self):
        if (len(self.data) == 0):
            return None
        return self.data.pop()


my_stack = MyStack()

my_stack.putStack("A")
my_stack.putStack("B")
my_stack.putStack("C")
my_stack.putStack("D")

print(my_stack.data)  # ['A', 'B', 'C', 'D'] 数据结构

while (len(my_stack.data) != 0):
    print(my_stack.pelletStack(), end=" ")  # 取值弹栈  D C B A  从结果就可以看出 是先进后出  后进先出的情况 成功模拟了栈的数据结构

print("")


# 用列表数据结构来模拟 队列数据结构：先进先出的情况
class MyQueue:
    def __init__(self):
        self.data = []

    def put(self, e):
        self.data.append(e)

    def get(self):
        if len(self.data) == 0:
            return None
        e = self.data[0]
        self.data.remove(e)
        return e


my_queue = MyQueue()

my_queue.put("A")
my_queue.put("B")
my_queue.put("C")
my_queue.put("D")
print(my_queue.data)  # ['A', 'B', 'C', 'D']

while len(my_queue.data) != 0:
    print(my_queue.get(), end="-")  # A-B-C-D- 先进先出

print("")

# 列表推导式
# 列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。
# 每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。
# 这里我们将列表中每个数值乘三，获得一个新的列表：

L1 = [2, 4, 6]

L1_ = [3 * x for x in L1]  # 此处用[]将for循环括起来，3*x 在for前面 对其for循环每个变量扩大3倍
print(L1_, type(L1_))  # [6, 12, 18]  <class 'list'>

# 可以理解为一下操作

L1_N1 = []
for x in L1:
    L1_N1.append(3 * x)
print(L1_N1)  # [6, 12, 18]

L2_ = (3 * x for x in L1)
print(L2_, type(L2_))

# 同理
L3_ = [[x, x * 3] for x in L1]
print(L3_)  # [[2, 6], [4, 12], [6, 18]]

# 去除每个元素的空格
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
L4_ = [s.strip() for s in freshfruit]  # 这里在for前面调用的是函数
print(L4_)  # ['banana', 'loganberry', 'passion fruit']

# 用if来过滤不需要的字段
L1 = [2, 4, 6, 8]

L5_ = [3 * x for x in L1 if x > 3]
print(L5_)  # [12, 18, 24]这里 在遍历数据的时候 先判定是否大于3 如果<3 该数据就被舍弃 然后在3*x对元素进行增倍，注意在if这种情况下 for 前面的3*x 这样的函数是不是能少的 或者会语法解析错误

# 以下是一些关于循环和其它技巧的演示：
v1 = [2, 4, 6]
v2 = [4, 3, -9]
v3 = []
for x in v1:
    for y in v2:
        v3.append(x * y)
print(v3)  # [8, 6, -18, 16, 12, -36, 24, 18, -54]

# 用python特有的循环来替代上面的操作
v4 = [x * y for x in v1 for y in v2]
print(v4)  # [8, 6, -18, 16, 12, -36, 24, 18, -54]

v5 = [x + y for x in v1 for y in v2]
print(v5)  # [6, 5, -7, 8, 7, -5, 10, 9, -3]

v6 = [v1[i] * v2[i] for i in range(len(v1))]
print(v6)  # [8, 12, -54]

# 复杂的列表推导
v7 = [str(round(355 / 113, i)) for i in range(1, 6)]
print(v7)  # ['3.1', '3.14', '3.142', '3.1416', '3.14159'] 对结果进行四舍五入 并保留 i位精度

# 以下实例将3X4的矩阵列表转换为4X3列表：
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

v8 = [[m[i] for m in matrix] for i in range(4)]
print(v8)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 元组和序列
# 元组由若干逗号分隔的值组成
# 如你所见，元组在输出时总是有括号的，以便于正确表达嵌套结构。在输入时可能有或没有括号， 不过括号通常是必须的（如果元组是更大的表达式的一部分）。

p1 = "A", "B", "C", "D"
print(type(p1), p1[0])  # <class 'tuple'> A

p2 = ("A", "B", "C", "D")
print(type(p2), ",", p2[1])  # <class 'tuple'> , B

# 定义一个空元组
p3 = ()
print(p3)  # ()

p4 = ("A")
print(type(p4))  # <class 'str'>

p5 = ("A",)  # 在元组中只有一个元素的时候，后面是需要添加,逗号
print(type(p5), p5[0])  # <class 'tuple'> A

# 集合
# 集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
# 可以用大括号{}创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典，下一节我们会介绍这个数据结构。
# 以下是一个简单的演示：

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # {'orange', 'banana', 'pear', 'apple'} 集合是没有重复的元素的，因此结果会过滤掉重复的元素

s1 = {}
print(type(s1))  # <class 'dict'> 因此创建一个空的集合，不能用{} 它表示一个空的字典类型

# 创建一个空的集合需要用set
s2 = set()
print(type(s2))  # <class 'set'>

# 创建集合也可以用set

s3 = set("abcaaee")
print(s3)  # {'b', 'c', 'e', 'a'}

s4 = set("abchhyyzz")
print(s4)  # {'z', 'c', 'h', 'y', 'a', 'b'}

s5 = s3 - s4  # 集合相见 表示前一个集合中的元素在后一个元素中不存在的元素 如 表示s3中的元素在s4中没有
print(s5)  # {'e'}
s6 = s4 - s3
print(s6)  # {'h', 'y', 'z'}

s7 = s3 | s4  # 可以理解 将2个集合合并在一起的元素 也就是s3 或s4有的元素
print(s7)  # {'a', 'b', 'c', 'y', 'e', 'h', 'z'}

s8 = s3 & s4  # 表示在s3与s4存在的交集，两个集合都同时存在的元素
print(s8)  # {'b', 'a', 'c'}

s9 = s3 ^ s4  # 表示2个集合中 其中一个没有 另外一个有的元素
print(s9)  # {'z', 'h', 'y', 'e'}

print("---------------------------------------------------")
# 集合也支持导推

s10 = {x for x in set("abdddfdfdavdcdsd") if x not in "abc"}
print(s10)  # {'d', 'v', 's', 'f'}

# 字典
# 另一个非常有用的 Python 内建数据类型是字典。
# 序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
# 理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。
# 一对大括号创建一个空的字典：{}。 dictionary 字典数据结构 可以理解成json
# 这是一个字典运用的简单例子：

# 声明一个字典
d1 = {'jack': 4098, 'sape': 4139}
print(type(d1))  # <class 'dict'>

d1["name"] = "mexican"
print(d1)  # {'jack': 4098, 'sape': 4139, 'name': 'mexican'}

print(d1["jack"])  # 4096

keys = d1.keys()
print(keys)  # 获取字典所有key dict_keys(['jack', 'sape', 'name'])
print(d1.values())  # 获取字典所有values #dict_values([4098, 4139, 'mexican'])

print(sorted(keys))  # ['jack', 'name', 'sape']对key进行排序

print('jack' in keys)  # True

# 构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对：

d2 = dict([("name", "ksea"), ("age", 27), ("email", "ksea@126.com")])
print(d2)  # {'name': 'ksea', 'age': 27, 'email': 'ksea@126.com'}

# 此外，字典推导可以用来创建任意键和值的表达式词典：
d3 = {x: x ** 2 for x in (2, 4, 6)}
print(d3)  # {2: 4, 4: 16, 6: 36}

# 如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便：
d4 = dict(sape=4139, guido=4127, jack=4098)  # {'sape': 4139, 'guido': 4127, 'jack': 4098}
print(d4)

# 遍历技巧
# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, "=", v)
    # 打印结果:
    # gallahad = the pure
    # robin = the brave

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, "=", v)

    # 打印结果:
    # 0 = tic
    # 1 = tac
    # 2 = toe


    # 同时遍历两个或更多的序列，可以使用 zip() 组合：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
    # 打印结果:
    # What is your name?  It is lancelot.
    # What is your quest?  It is the holy grail.
    # What is your favorite color?  It is blue.



    # 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：
for i in reversed(range(1, 10, 2)):
    print(i, end=" ")  # 9 7 5 3 1
print("")

# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f, end=" ")  # apple banana orange pear
print("")

#列表推导式的执行顺序：各语句之间是嵌套关系，左边第二个语句是最外层，依次往右进一层，左边#第一条语句是最后一层。
#[x*y for x in range[1,5] if x > 2 for y in range[1,4] if x < 3]
#他的执行顺序是
#for x in range[1,5]
#   if x > 2
#        for y in range[1,4]
#            if x < 3
#                x*y

