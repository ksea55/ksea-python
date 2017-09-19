# Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

# for循环的一般格式如下：
# for <variable> in <sequence>:
#   <statements>
# else:
#    <statements>

s1 = "abcdefg";  # 迭代一个字符串
for s in s1:
    print(s, end=",")  # a,b,c,d,e,f,g,

print(" ")

# 遍历一个列表

seq1 = ["baidu", "taobao", "360", "google", "fackbook"]
for s in seq1:
    print(s, end="/")  # baidu/taobao/360/google/fackbook/

print("")

# for循环迭代跳出循环体

for s in seq1:
    if s == "google":
        print("已经找到google!")
        break

print("")

for s1 in seq1:
    print(s1, end="-")
else:
    print("便利结束")
print("for is over")

