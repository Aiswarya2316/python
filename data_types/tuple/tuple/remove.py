t=1,2,3,4,4,4
a=list(t)
unique_list = []
for item in a:
    if item not in unique_list:
        unique_list.append(item)
t=tuple(unique_list)        
print(t)