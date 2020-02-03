nums=[]
def foo(a,b,c,d):
    srednee=(a+b+c+d)/4

    nums.append(a)
    nums.append(b)
    nums.append(c)
    nums.append(d)
    maximum=max(nums)
    return srednee,maximum
while True:
 print(foo(int(input()),int(input()),int(input()),int(input())))