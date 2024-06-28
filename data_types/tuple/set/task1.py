print("1.Addin_zoo\n2.Addin_python\n3.view_students\n4.viewduplicate_student\n5.different_names")
zoology=set()
python=set()
while True:
    choice=int(input("Enter your choice:"))
    if choice==1:
        a=int(input("Enter the limit:"))
        for i in range(a):
            b=str(input("Enter the name"))
            zoology.add(b)

    elif choice==2:
        a=int(input("Enter the limit:"))
        for i in range(a):
            b=str(input("Enter the name"))
            python.add(b)  

    elif choice==3: 
        print('students in science :',zoology)
        print('students in programing :',python)

    elif choice==4: 
        print('common students are :')
        print(zoology.intersection(python))
    
    elif choice==5: 
        print('different students are :')
        print(python.difference(zoology))
    
               

