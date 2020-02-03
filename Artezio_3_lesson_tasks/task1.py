my_list=[2,6,1,5]


def squares(a):
    new_list=[]
    for item in a:
     new_list.append(item**2)
    return new_list

print(squares(my_list))

def chetnoe(a):
    new_list=[]
    i=1
    for item in a:
        if i%2==0:
            new_list.append(item)
        i=i+1
    return new_list

print(chetnoe(my_list))

def kub(a):
    new_list=[]
    i=1
    for item in a:
        if i%2!=0 and item%2==0:
            new_list.append(item**3)
        i=i+1
    return new_list

print(kub(my_list))
