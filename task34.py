# print
# 1
# 12
# 123 

for i in range(1,4):
    for j in range(i):
      print(j+1,end="")
    print() 


# print
# 1
# 22
# 333  

for i in range(1, 4):
    for j in range(i):
        print(i, end=" ")
    print()


# print
# 1
# 21
# 321

for i in range(1, 4):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
