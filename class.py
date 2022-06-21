class MyClass():
    def __init__(self, x, y):
        self.x = x
        self.y = y

o1 = MyClass(9, 8)
print(o1.x)
print(o1.__dict__)