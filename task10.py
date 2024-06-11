a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
d=int(input("Enter fourth number"))

if a>b:
    if a>c:
        if a>d:
            print("greatest number is:",a)

        else:
            print("greatest number is:",d)

    else:
        if c>d:
            print("greatest number is:",c) 

        else:
            print("greatest number is:",d) 

else:

    if b>c:
        if b>d:
         print("greatest number is:",b)

        else:
            print("greatest number is:",d) 

    else:
        if c>d:
            print("greatest number is:",c)

        else:
            print("greatest number is:",d)    

        