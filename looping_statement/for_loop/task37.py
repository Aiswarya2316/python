# print
# A 
# AB 
# ABC 

a=65
for i in range(1,4):
    for j in range(i):
      print(chr(a+j),end=" ")
    print() 


# print
# A 
# BB 
# CCC 


for i in range(1, 4):
    a=65
    for j in range(i):
        print(chr((a-1)+i), end=" ")
    print()


# print
# A 
# BA 
# CBA 

a=65
for i in range(1, 4):
    for j in range(i, 0, -1):
        print(chr((a-1)+j), end=" ")
    print()

    #    OR

a=65
for i in range(1,4):
    b=a
    for j in range(i):
        print(chr(b) ,end=" ")
        b-=1
    print()
    a+=1    
