# n = 3  

# for i in range(n):

#     for j in range(i, -1, -1):
#         print(chr(65 + j), end=" ")
#     print()  




n=65 

for i in range(3):
    a=1
    for j in range(3):
        if i == j:
            print(a, end=" ")
        else:
            print(chr(n), end=" ")
    print() 
    n+=1 





# n = 3  

# for i in range(n):
#     if i % 2 == 0:  
#         for j in range(n):
#             print(chr(65 + j), end=" ")
#     else:  
#         for j in range(n - 1, -1, -1):
#             print(chr(65 + j), end=" ")
#     print()  
