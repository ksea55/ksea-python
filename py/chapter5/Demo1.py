class Student:
    # 定义基本属性
    name = ""  # 这种定义方式相当于java的public
    age = 0  # 这种定义方式相当于java的public
    __email = ""  # 在python中私有属性是需要用2个下划线__开头 相当于在java中的private

    _sno = 0  # 前面加一个下划线_表示当前属性是受保护的 相当于java中的protected,子类是可以被继承的

    def show(self, name, age, email, sno):
        self.name = name
        self.age = age
        self.__email = email
        self._sno = sno


s = Student()
s.show("jacky", 21, "jacky@126.com", 1344234)
print("name:", s.name, "age:", s.age)  # 在这里想要访问私有属性就访问不到
