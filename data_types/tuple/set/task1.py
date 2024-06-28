print("1.Addin_zoo\n2.Addin_python")
zoology=set()
python=set()
while True:
    choice=int(input("Enter your choice:"))
    a=int(input("Enter the limit:"))
    if choice==1:
        for i in range(a):
            b=str(input("Enter the name"))
            zoology.add(b)

    if choice==2:
        for i in range(a):
            b=str(input("Enter the name"))
            python.add(b)       

