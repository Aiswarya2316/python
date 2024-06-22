         # print list avoid duplicate

# my_list = [1, 2, 3, 4, 3, 4]
# for i in range(len(my_list)):
#     if my_list[i] not in my_list[:i]:
#         print(my_list[i])

              #or

# original=[1,2,3,2,3]
# unique=[]
# for item in original:
#     if item not in unique:
#         unique.append(item)
# print(unique)


    # print no and str find sum of no

# L=[10,20,30,40,'a','b','c','d'] 
# print(" list:", L)
# sum=0
# for i in  L:
#    if  type(i) in (int,float):
#      sum += i
# print("sum is:",sum)

            #or

L=[10,20,30,40,'a','b','c','d'] 
print(" list:", L)
sum=0
for i in  L:
   if  type(i)==int or type(i)==float:
     sum += i
print("sum is:",sum)


    # print the largest number in the list

L=[10,20,30,40,50]
print(L)
large=max(L)
print(large)

        #or

L=[10,40,30,50,20]
L.sort()
print(L[-1])
print(L)