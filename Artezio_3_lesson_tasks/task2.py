def foo(a):
    count = 0
    for i in a:
        if isinstance(i, list):
            count += foo(i)
        else:
            count += i
    return count

print(foo([3, 4, [5, 6, 0],[2]]))

