dtls=[{"name":"anu","age":20},{"name":"akhil","age":25},{"name":"achu","age":22},{"name":"ammu","age":24}]
for i in range(0):
    name=input("name")
    age=int(input("age"))
    dtls.append({"name":name,"age":age})
print("{:<10}{:<6}".format("name","age"))
print('_'*20)
for i in dtls:
    print("{:<10}{:<6}".format(i["name"],i["age"]))

