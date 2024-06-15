# print
# *
# * *
# * * *

row = 3 
for i in range(1, row + 1):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(row - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# print
# 1 
# 1 2
# 1 2 3
# 1 2
# 1

a=3
for i in range(1,a+1):
    for j in range(i):
        print(j+1,end=" ")
    print()
    

for i in range(a-1,0,-1) :
    for j in range(i):
        print(j+1 , end=" ")
    print()   

# print
# A 
# AB 
# ABC 
# AB 
# A     

b=3
a=64
for i in range(1,b+1):
    for j in range(i):
        print(chr((a+1)+j),end=" ")
    print()
    

for i in range(b-1,0,-1) :
    for j in range(i):
        print(chr((a+1)+j) , end=" ")
    print() 