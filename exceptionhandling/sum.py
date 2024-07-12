
# l = [1, 2, 'a', 'c', 'b', 'hello']
# sum = 0
# try:
#     for i in l:
    
#     # if isinstance(i, int) or (isinstance(i, str) and i.isdigit()):
#         sum += int(i)
# except:        
#     print("The sum of integers in the list is:", sum)



l = [1, 2, 'a', 'c', 'b', 'hello']
sum = 0
for i in l:
    try:
        sum +=i
    except:  
        pass      
print("The sum of integers in the list is:", sum)
