l=[1,2,3,4,5,6,7,8,9,10,2,4,6,8,10]
data=filter(lambda a:a%2==0,l)
print(list(data))





def fun1(a):
    return a%2==0
data1=filter(fun1,l)
print(list(data1))





l=["apple","mango"]
data=filter(lambda a:a[0]=='a',l)
print(list(data))





de