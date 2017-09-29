# 类的专有方法：

class Base:
    # 构造函数，在生成对象时调用
    def __init__(self):
        print("this is constructor")

    # 析构函数，释放对象时使用
    def __del__(self):
        print("this is release object")


b = Base()

"""
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__div__: 除运算
__mod__: 求余运算
__pow__: 乘方
"""
