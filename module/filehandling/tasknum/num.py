f=open("python/module/filehandling/tasknum/mul.txt","x")
def print_multiplication_table(number, upto=10):
    """
    Prints the multiplication table of the given number up to the specified limit.
    
    Parameters:
    - number (int): The number whose multiplication table is to be printed.
    - upto (int): Optional. The upper limit for the multiplication table. Default is 10.
    """
    print(f"Multiplication table of {number}:")
    for i in range(1, upto + 1):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print_multiplication_table(num)
