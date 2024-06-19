a=int(input('enter a value'))
i=1
while i<=10:
    print(i,'*',a,'=',a*i)
    i+=1


a=int(input('enter a number'))
rev=0
while a>0:
    d=a%10
    rev=(rev*10)+d
    a//=10
    if a==0:
        break
print(rev)


a=int(input('enter a number'))
sum=0
while a>0:
    d=a%10
    a//=10
    sum+=d
print(sum)


a='welcome'
l=len(a)
i=0
while i<l:
    print(a[i])
    i+=1


a='welcome'
l=len(a)
i=0
rev=''
while i<l:
    rev=a[i]+rev
    i+=1
print(rev)


a=0
b=1
i=0
while i<=10:
    print(a)
    c=a+b
    a=b
    b=c
    i+=1