# print
# 0
# 12
# 345

# a = 0
# for i in range(1, 4):
#     for j in range(i):
#         print(a, end=" ")
#         a += 1
#     print()


# print
# 0
# 22
# 444

# for i in range(3):
#     for j in range(i + 1):
#         print(i * 2, end=" ")
#     print()


# print
# 0
# 14
# 91625

for i in range(3):
    for j in range(i + 1):
        print(j**2, end=" ")
    print()
