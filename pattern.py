rows = 6

for i in range(rows):
    for j in range(i):
        print((i+j)% 2,end=' ')
    print()


row=6
for i in range(row):
    for j in range(i+1):
        if i%2==0:
            print("#", end= ' ') 
        else:
            print("+", end= ' ') 
    print()   


  