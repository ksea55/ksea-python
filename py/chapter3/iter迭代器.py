# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。。
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
# 字符串，列表或元组对象都可用于创建迭代器：

str1 = "abcdef";
iter1 = iter(str1)
print(next(iter1))  # a
print(next(iter1))  # b

# for来迭代iter

list1 = ["A", "B", "C", "D", "E"]
iter2 = iter(list1)
for i in iter2:
    print(i, end=" ")  # A B C D E
print("")
print("==============================================")

# 使用while来进行iter迭代器
list2 = ["A", "B", "C", "D", "E"]
iter3 = iter(list2)
while True:
    try:
        i = next(iter3)
        print(i, end=" ")
    except StopIteration:
        import sys

        sys.exit()

        # 打印结果: A B C D E

print("")
print("======================================================")

