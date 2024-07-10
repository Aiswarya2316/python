f = open("python/module/filehandling/tasknum/table2.txt", "w")
a = int(input("Enter the number :"))
for i in range(1,a+1):
    for j in range(1, 11):
        b = str(j) + " * " + str(a) + " = " + str(j * a) + "\n"
        f.write(b)
    a-=1