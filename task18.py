print("Print the odd numbers and its sum")
a=int(input("Enter the starting value"))
b=int(input("Enter the ending value"))
sum=0

for i in range(a,b):
    
    if i%2==1:
       sum+=i
       print(i)
print(sum)    
