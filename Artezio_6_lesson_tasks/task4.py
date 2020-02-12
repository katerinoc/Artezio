"""Task 4"""

A = iter([1, 2])


def cycle(arg):
    _list = []
    for item in arg:
        _list.append(item)
        yield item
    count = 0

    while True:
        yield _list[count]
        count = count + 1
        if count >= len(_list):
            count = 0


C = cycle(A)
print(next(C))
print(next(C))
print(next(C))
