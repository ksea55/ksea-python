# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# 语法
# 以下是 enumerate() 方法的语法:
# enumerate(sequence, [start=0])
# 参数
# sequence -- 一个序列、迭代器或其他支持迭代对象。
# start -- 下标起始位置。


seq1 = ["baidu", "taobao", "360", "google", "fackbook"]

e1 = enumerate(seq1)
print(list(e1))  # [(0, 'baidu'), (1, 'taobao'), (2, '360'), (3, 'google'), (4, 'fackbook')]

for index, val in enumerate(seq1):
    print("{index}:{val}".format(index=index, val=val))
    # 打印结果:
    # 0:baidu
    # 1:taobao
    # 2:360
    # 3:google
    # 4:fackbook
print("-------------------------------------------------")

# 当然使用range函数也是可以同样实现
for index in range(len(seq1)):
    print("{0}:{1}".format(index, seq1[index]))
    # 打印结果:
    # 0:baidu
    # 1:taobao
    # 2:360
    # 3:google
    # 4:fackbook

# 求1-100之间的和 我们就可以利用range函数
sum = 0;
for s in range(1, 101):
    sum += s;
print(sum)  # 5050


