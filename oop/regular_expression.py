a="welcome"
import re
# print(re.sub("w","s",a))

# print(re.split("e",a))

# print(re.sub("welcome","python",a))

# print(re.search("z",a))

# if re.search("l",a):
#     print("yes")
# else:
#     print("nop")            

# print(re.search('[a-m]',a) )  

# a="abcde"

# print(re.search("a.",a))

# print(re.search('b..',a))

# print(re.search('b.*',a))

# print(re.search('b.+',a))

# print(re.search('b.?',a))

# print(re.search('[a-z].',a) )  

# print(re.search('[a-z].+',a) )

# print(re.search('[a-z].*',a) )  

# print(re.search('[A-Z].?',a) )  

# print(re.search('[a-z]..',a) )  

a="AabcBd123456"
print(re.search('[a-z]',a))

print(re.search('[a-z][0-9]',a) )

print(re.search('[A-Z][a-z][0-9]',a))

