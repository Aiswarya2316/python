# number={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}
# num=int(input("Enter a number:"))
# for num in number:
#     i=0
#     print(i[num])




# number = {
#     0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
#     5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"
# }
# num = int(input("Enter a number between 0 and 10: "))
# if num in number:
#     print(number[num])
# else:
#     print("Number out of range. Please enter a number between 0 and 10.")


number = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"
}
for i in range(len(number)):
    print(number[i], number[i])