# print
# ABCD
# ABCD
# ABCD

for i in range(3):
    a=65
    for j in range(4):
        print(chr(a), end=" ")
        a+=1
    print()


# print
# ABC
# DEF  
# GHI

a=65  
for i in range(3):
    for j in range(3):
      print(chr(a),end=" ")
      a+=1
    print()    


# print
# AAA
# BBB
# CCC

for i in range(3):
    a=65 
    for j in range(3):     
      print(chr(a+i) , end=" ")
    print()  