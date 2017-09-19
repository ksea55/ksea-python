# 用while求1-100之间的和
counter = 1;
num = 100;
sum = 0;
while counter <= num:
    sum += counter;
    counter += 1;
print("{0}到{1}之间的总和:{2}".format(1, num, sum))  # 1到100之间的总和:5050

# 在python中，while语句与java中一样 除了语法是用: ,python中的while还有一个 while...else语法



a1 = 1;
while a1 < 5:
    print("a1小于5!")
    a1 += 1;
else:
    print("a1 已经大于等于5了!")
