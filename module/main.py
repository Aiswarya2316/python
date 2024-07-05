from reg import *
data=[]
while True:
    print("1.add\n2.display\n3.update\n4.dalete\n5.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        add(data)
