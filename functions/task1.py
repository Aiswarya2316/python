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





a=20
def fun4():
    global b
    print("global",b)
    c=30
    return c,40,50
c1,d1,f1=fun4()
print("return",c1,d1,f1)