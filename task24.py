a=int(input("Enter a number"))
reverse_number=0

for digit in str(a)[::-1]:
    reverse_number=reverse_number*10 + int(digit)
print("Reverse number is:",reverse_number)