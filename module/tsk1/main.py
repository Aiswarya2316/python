from reg import *
from dis import *
from upd import *
data=[]
while True:
    print("1.add\n2.display\n3.update\n4.dalete\n5.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        add(data)
    elif ch==2:
        dis(data) 

    elif ch == 3:
        up(data)
       
