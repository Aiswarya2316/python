# number={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}
# num=int(input("Enter a number:"))
# for num in number:
#     i=0
#     print(i[num])


num={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
a=int(input("enter the number :"))
result = []
for digit in str(a):
    result.append(num[int(digit)])

print(" ".join(result))


               #or


num = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
}

a = int(input("Enter a number : "))

if 0 <= a <= 9:
    for i in range(a + 1):  
        print(num[i])
else:
    print("Invalid input.")



                #or



num={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
a=int(input("enter the number :"))
a_str = str(a)
result = ""
for char in a_str:
    digit = int(char)
    if digit in num:
        result += num[digit] + " "
print(result.strip())                