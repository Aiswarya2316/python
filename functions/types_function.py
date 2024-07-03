def add(a,b,c):
    return a+b-c

print(add(10,20,30))
print(add(40,50,60))





def add(name,age=21):
    return name,age

print(add('abc',20))
print(add('aisu'))





def add(name,age):
    print("name:",name)
    print("age:",age)

add("ammu",21)    
add(name="achu",age=21)






def add(*a):
    return(a)

print (add("achu","ammu","anu","devu","malu"))
print (add())






def add(*a):
    return(a)