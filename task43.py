      # break

print("1.Add\n2.Sub\n3.Mul\n4.Div\n5.Mod\n6.Exit")
while True:
    choice=int(input("Enter your choice:"))
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    if choice==1:
     print("add:",a+b)
    elif choice==2:
     print("sub:",a-b)    
    elif choice==3:
     print("mul:",a*b)
    elif choice==4:
     print("div:",a/b)
    elif choice==5:
     print("mod:",a%b)  
    elif choice==6:
      print("invalid")  
      break     

