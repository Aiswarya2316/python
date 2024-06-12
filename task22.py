a = int(input("Enter number: "))
a_is_prime = True

if a < 2:
    a_is_prime = False
else:
    a_is_prime = True

    for i in range(2, a):
        if a % i == 0:  
           a_is_prime = False
        break


if a_is_prime:
    print(a, "is a prime number.")
else:
    print(a, "is not a prime number.")
