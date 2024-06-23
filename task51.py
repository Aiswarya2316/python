          # print largest number of a list using swap

numbers = [5, 3, 8, 6, 2, 9, 1]
print("List of numbers:", numbers)
for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if numbers[i] < numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp
largest_number = numbers[0]
print("Largest number in the list:", largest_number)

                 #or

numbers = [15, 22, 8, 19, 42, 3, 89, 16, 56, 1]
print(numbers)
largest_number = numbers[0]
for i in range(1, len(numbers)):
    if numbers[i] > largest_number:
        largest_number = numbers[i]
print("The largest number in the list is:", largest_number)                 
