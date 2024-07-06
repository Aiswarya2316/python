from reg import *
from dis import *
from upd import *
from delet import *
data=[{"id": "1", "name": "Alice", "age": "30", "place": "New York"},
    {"id": "2", "name": "Bob", "age": "25", "place": "Chicago"},]
while True:
    print("1.add\n2.display\n3.update\n4.dalete\n5.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        add(data)
    elif ch==2:
        dis(data) 
    elif ch == 3:
        up(data)
    elif ch == 4:
        dele(data)
    elif ch == 5:
        print("You had exited")
        break
    else:
        ("Invalid input")
