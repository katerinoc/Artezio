"""Task 2"""


class MyObject:

    an = 5

    def __init__(self, a, b):
        self.a = a
        self.b = b


A = MyObject(3, 2)
print([item for item in dir(MyObject) if not item.startswith('_')])
