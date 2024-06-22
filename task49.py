print("1.Add\n2.display\n3.update\n4.delete\n5.exit")
names=[]
while True:
    choice=int(input("Enter your choice:"))
    a=int(input("Enter the limit:"))
    if choice==1:
     for i in range(a):
      b=str(input("Enter the name"))
      names.append(b)

    elif choice==2:
     for i in names:
      print(i)

    elif choice==3:
      oldname=str(input("Enter old name"))
      if oldname in names:
        b=str(input("Enter the updation"))
        pos=names.index(oldname)
        names[pos]=b
        print("updation is :",names) 
      else:
        print("Name not found")           

    elif choice==4:
     del names[a]
     print(names)

    elif choice==5:
     print("exit:") 
     break     
    