a=int(input("Enter a number"))
rev=0

for i in range(a):
    digit=a%10
    rev=(rev*10)+digit
    a//=10
    if a==0:
        break
print(rev)