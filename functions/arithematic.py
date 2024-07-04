
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
pro=lambda a,b:a*b

div=lambda a,b:a/b

def num():
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    return a,b

while True:
    print("1.add\n2.sub\n3.pro\n4.div")
    ch=int(input("Enter your choice:"))
    if ch==1:
        a,b=num()
        print(add(a,b))
    elif ch==2:
        a,b=num() 
        print(sub(a,b))
    elif ch==3:
        a,b=num()
        print(pro(a,b))
    elif ch==4:
        a,b=num()
        print(div(a,b))
    elif ch==5:
        break    



