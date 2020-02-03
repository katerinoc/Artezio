def foo(a):
   a = a.split()
   return min(list(map(lambda item:abs(float(item)), a)))

print(foo(input()))