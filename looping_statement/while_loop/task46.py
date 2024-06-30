    #    "remove"

my_list = [1, 2, 3, 4, 3, 5]
value_to_remove = 3
while value_to_remove in my_list:
    my_list.remove(value_to_remove)
print(my_list)


        #   "insert"

my_list = [1, 2, 3, 4, 5]
print("Current List:", my_list)
value = input("Enter the value to insert: ")
position = int(input("Enter the position to insert the value at: "))
my_list.insert(position, value)
print("Updated List:", my_list)


        #  "append"

my_list = [1, 2, 3, 4, 5]
new_value = input("Enter a value to append: ")
my_list.append(new_value)
print("Updated list:", my_list)


        # extend

input_list = [6, 7, 8]
list_values = [1, 2, 3, 4, 5]
list_values.extend(input_list)
print(list_values)



        # pop

fruits = ['apple', 'banana', 'cherry', 'date']
popped_element = fruits.pop()
print("Popped element:", popped_element)  
print("Updated list:",fruits)  


     # clear

my_list = [1, 2, 3, 4]
my_list.clear()
print(my_list)  

