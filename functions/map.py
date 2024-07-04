l=[1,2,3,4,5,6,7,8,9,10]
data=map(lambda a:a**2,l)
print(data)
print(list(data))


def fun1(a):
    return a**2
data1=map(fun1,l)
print(list(data1))
