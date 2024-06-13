start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            print(num)