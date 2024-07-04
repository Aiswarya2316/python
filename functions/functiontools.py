import functools
l=[1,2,3,4,5]
data=functools.reduce(lambda total,value:total*value,l)
print(data)
