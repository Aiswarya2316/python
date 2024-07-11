       #append

# f=open("new.txt","a")
# f.write("python")

      #read

# f=open("new.txt","r")
# print(f.read())


# f=open("new.txt","r")
# print(f.read(4))
# print('-'*20)
# print(f.read(4))

       #readline

# f=open("new.txt","r")
# print(f.readline(4))

       #readlines

# f=open("new.txt","r")
# print(f.readlines(10))
# print('-'*20)




f=open("new.txt","r")
l=len(f.readlines())
f.seek(0)
for i in range(l):
    a=f.readline().strip()
    print(a[::-1])
