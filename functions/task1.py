# print("start")
# def fun1():
#     print("heloo")
#     print("welcome")
# fun1()
# print("stop")





# a=30 #global
# def fun2():
#     a=20  #local
#     print("welcome",a)
# fun2()
# print(a)





# def fun3():
#     global b
#     b=20
#     print("global",b)
# fun3()
# print(b)    





# a=20
# def fun4():
#     global b
#     print("global",b)
#     c=30
#     return c,40,50
# c1,d1,f1=fun4()
# print("return",c1,d1,f1)





            #   type of function

# def add(a,b,c):
#     return a+b-c

# print(add(10,20,30))
# print(add(40,50,60))





# def add(name,age=21):
#     return name,age

# print(add('abc',20))
# print(add('aisu'))





# def add(name,age):
#     print("name:",name)
#     print("age:",age)

# add("ammu",21)    
# add(name="achu",age=21)





# def add(*a):
#     return a

# print (add("achu","ammu","anu","devu","malu"))
# print (add())




def add(**a):
    return a

print(add(name="ammu",age=21,place="ekm",state="kerala",capital="trivandram"))