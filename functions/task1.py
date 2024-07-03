# print("start")
# def fun1():
#     print("heloo")
#     print("welcome")
# fun1()
# print("stop")



a=30 #global
def fun2():
    a=20  #local
    print("welcome",a)
fun2()
print(a)