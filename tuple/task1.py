t=1,2,3
print(t)
t1=(1,)
print(type(t1))




t=1,2,3,4,5
for i in t:
    print(i)
a=int(input('enter a number :'))
if a in t:
    print('value available')
    print()
else:
    print('invalid value')
    print()

        # tuple methods
t=1,2,3,4,5,4,44,4,4,4,4
print(t.index(4))
print(t.count(4))

f=('abc',123,['name',20])
f[2][1]=21
print(f[2])

t=1,2,3
a=list(t) #typecasting
a[2]='a'
t=tuple(a)
print(t)

t=1,2,3,4,4,4
a=list(t)
unique_list = []
for item in a:
    if item not in unique_list:
        unique_list.append(item)
t=tuple(unique_list)        
print(t)