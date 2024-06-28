 # tuple methods
t=('abc',123,['name',20])
print(t.index(4))
print(t.count(4))
t[2][1]=21
print(t[2])


    #   ad & update

t=1,2,3
a=list(t) 
a[2]='a'
t=tuple(a)
print(t)

