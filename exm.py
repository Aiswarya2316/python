# n = 3  # Number of rows

# for i in range(n):
#     # Inner loop to print characters in reverse order
#     for j in range(i, -1, -1):
#         print(chr(65 + j), end=" ")
#     print()  # New line after each row




# n = 3  # Number of rows

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             print(1, end=" ")
#         else:
#             print(chr(65 + j), end=" ")
#     print()  # New line after each row





n = 3  # Number of rows

for i in range(n):
    if i % 2 == 0:  # For even rows (0, 2)
        for j in range(n):
            print(chr(65 + j), end=" ")
    else:  # For odd row (1)
        for j in range(n - 1, -1, -1):
            print(chr(65 + j), end=" ")
    print()  # Move to
