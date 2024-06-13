a=str(input("Enter a word"))
reverse_number=""

for digit in str(a)[::-1]:
    reverse_number=reverse_number + str(digit)
print("Reverse number is:",reverse_number)