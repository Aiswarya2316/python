def add_names_to_file(filename, names):
    try:
        # Open file in append mode
        with open(filename, 'a') as file:
            for name in names:
                file.write(name + '\n')
        print(f"Names successfully added to {filename}")
    except IOError:
        print(f"Error: Could not open {filename} for writing")

# Example usage
filename = 'names.txt'
names_to_add = ['Alice', 'Bob', 'Charlie']

add_names_to_file(filename, names_to_add)
