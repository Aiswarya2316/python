# def count_words_in_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#             words = content.split()
#             return len(words)
#     except FileNotFoundError:
#         print(f"Error: The file '{filename}' was not found.")
#         return -1
#     except IOError:
#         print(f"Error: There was an IO error while reading the file '{filename}'.")
#         return -1

# # Example usage:
# file_name = 'new.txt'  # Replace with your file path
# word_count = count_words_in_file(file_name)

# if word_count != -1:
#     print(f"The file '{file_name}' contains {word_count} words.")



# f=open("new.txt","r")
# l=len(f.readlines())
# f.seek(0)
# word=0
# for i in range(l):
#     a=f.readline().strip()
#     for j in a:
#         if j==' ' :
#             word+=1
#     print(a[::-1])
#     word+=1
# print(word)


#             #letter

# file_name = 'new.txt'  # Replace with your file path
# letter_count = 0

# try:
#     with open(file_name, 'r') as file:
#         for line in file:
#             for char in line:
#                 if char.isalpha():
#                     letter_count += 1
# except FileNotFoundError:
#     print(f"Error: The file '{file_name}' was not found.")
# except IOError:
#     print(f"Error: There was an IO error while reading the file '{file_name}'.")

# print(f"The file '{file_name}' contains {letter_count} letters.")



                #or

# f=open("new.txt","r")
# l=len(f.readlines())
# f.seek(0)
# word=0
# letters=0
# for i in range(l):
#     a=f.readline().strip()
#     for j in a:
#         if j=='' :
#             word+=1
#         else:
#             letters+=1    
#     print(a[::-1])
#     word+=1
# print(word)
# print(letters)







# f=open("new.txt","r")
# l=len(f.readlines())
# # f.seek(0)
# word=0
# # letters=0
# for i in range(l):
#     a=f.readline().strip()
#     for j in a:
#         if word.isupper():
#                     print(f"Uppercase word: {word}")
#         elif word.islower():
#                     print(f"Lowercase word: {word}")  
# #     print(a[::-1])
# #     word+=1
# # print(word)
# # print(letters)




f=open("new.txt","r")
l=len(f.readlines())
f.seek(0)
word=0
letters=0
capt=0
for i in range(l):
    a=f.readline().strip()
    for j in a:
        if j=='' :
            word+=1
        else:
            letters+=1   
            if j.isupper():
                capt+=1
    print(a[::-1])
    word+=1
print("words",word)
print("letters",letters)
print("capitals",capt)
print("smallletters",letters-capt)