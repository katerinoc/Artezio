"""Task 1"""


class EvenIterator:

    """Constructor"""
    def __init__(self, my_list):
        self.my_list = my_list
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self.my_list):
            raise StopIteration
        self.counter += 1

    def current(self):
        if self.counter < len(self.my_list):
            if (self.counter+1) % 2 == 0:
                return self.my_list[self.counter]


A = [1, 2, 3, 4, 5, 5]
MY_OBJ = EvenIterator(A)
while True:
    try:
        MY_OBJ.__next__()
    except StopIteration:
        break
    print(MY_OBJ.current())
