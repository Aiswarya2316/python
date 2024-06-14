
# for i in range(3):
#   for i in range(4):
#     print(i,end="\t")
#   print()


# for i in range(3):
#     for j in range(3):
#       print(i,end="\t")
#     print()

# a=0
# for i in range(3):
#     for j in range(3):
#         print(i*3+j,end="\t")
#         print(a,end="\t")
#         a+=1
#     print()


for i in range(4):
    a=2
    for j in range(3):
      if i % 2 == 0:
        # for j in range(3):
        print(j, end=" ")
      else:
        # for j in range(2, -1, -1):
        print(a, end=" ")
        a-=1
    print()

