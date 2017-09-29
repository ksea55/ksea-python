class PythonOOP:
    i = 12345;

    def hello(self):
        print("hello world")


p = PythonOOP()
print("i:", p.i)
p.hello()


class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print("x:", self.x, "y:", self.y)
        return "hello"


c = Complex(1, 2)
print(c, c.x, c.y)
