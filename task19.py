print("Print the odd,even,natural numbers  sum")
a=int(input("Enter the starting value"))
b=int(input("Enter the ending value"))

sum=0
oddsum=0
evensum=0

for i in range(a,b+1):
    sum+=i 
    if i%2==1:
     oddsum+=i  
    else:
     evensum+=i
     
print("natural sum:",sum)             
print("even sum:",evensum)
print("natural sum:",oddsum)        
        