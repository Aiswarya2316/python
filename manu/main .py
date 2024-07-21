import calculator 

def main():                                               
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", calculator.add(num1, num2))
    elif choice == '2':
        print("Result:", calculator.subtract(num1, num2))
    elif choice == '3':
        print("Result:", calculator.multiply(num1, num2))
    elif choice == '4':
        print("Result:", calculator.divide(num1, num2))
    else:
        print("Invalid input")

if __name__ == "_main_":
    main()