# range()函数 如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，

r1 = range(5)
print(r1)  # range(0, 5) 生成0-5之间的字数序列
for r in r1:
    print(r, end=",")  # 0,1,2,3,4,

print("")
for r in range(5):
    print(r, end="-")  # 0-1-2-3-4-

print("")

# 指定生成某个区间的数字序列
for r in range(5, 10):
    print(r, end=":")  # 5:6:7:8:9:
print("")

# 指定在某个区间的数字序列，并按指定的值进行累加
for r in range(1, 10, 2):  # 指定生成1-10之间的数字序列，并按2进行增加
    print(r, end="*")  # 1*3*5*7*9*
print("")
site = ["baidu", "google", "taobao", "facebook"]
# 遍历site打印结果与序列号
for index in range(len(site)):
    print(index, ":", site[index])
# 打印结果:
# 0: baidu
# 1: google
# 2: taobao
# 3: facebook
