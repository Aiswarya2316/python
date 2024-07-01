# dtls=[{"name":"anu","age":20},{"name":"akhil","age":25},{"name":"achu","age":22},{"name":"ammu","age":24}]
# for i in range(0):
#     name=input("name")
#     age=int(input("age"))
#     dtls.append({"name":name,"age":age})
# print("{:<10}{:<6}".format("name","age"))
# print('_'*20)
# for i in dtls:
#     print("{:<10}{:<6}".format(i["name"],i["age"]))

# print("age>22")
# print("{:<10}{:<6}".format("name","age"))
# for i in dtls:
#     if i["age"]>=22:
#       print("{:<10}{:<6}".format(i["name"],i["age"])) 

# print("age<22")
# print("{:<10}{:<6}".format("name","age"))
# for i in dtls:
#     if i["age"]<22:
#       print("{:<10}{:<6}".format(i["name"],i["age"])) 



                      #OR


children = [
    {"name": "Alice", "age": 18},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 15},
    {"name": "David", "age": 25},
    {"name": "Eve", "age": 19}
]
print(children)

print("Name\t\tAge")
print("--------------------")
print("above 20:")

for child in children:
    if child["age"] >= 20:
        print(f"{child['name']}\t\t{child['age']}")
        

print()


print("Name\t\tAge")
print("--------------------")
print("below 20:")

for child in children:
    if child["age"] < 20:
        print(f"{child['name']}\t\t{child['age']}")


