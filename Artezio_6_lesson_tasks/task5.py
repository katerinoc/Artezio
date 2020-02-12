"""Task 5"""

A = [1, 2, 3]
B = [1, 6]


def chain(*args):
    for i in args:
        for item in i:
            yield item


C = chain(A, B)
print(next(C))
print(next(C))
print(next(C))
print(next(C))
print(next(C))
