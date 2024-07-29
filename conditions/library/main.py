from library import Library

def main():
    library = Library()
    
    while True:
        print("\n1. Register\n2. Login\n3. Add Book\n4. Borrow Book\n5. Return Book\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            library.register_user(username, password)
        
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = library.login_user(username, password)
            if user:
                while True:
                    print("\n1. Borrow Book\n2. Return Book\n3. Logout")
                    user_choice = input("Enter your choice: ")
                    if user_choice == '1':
                        title = input("Enter book title: ")
                        library.borrow_book(user, title)
                    elif user_choice == '2':
                        title = input("Enter book title: ")
                        library.return_book(user, title)
                    elif user_choice == '3':
                        break
                    else:
                        print("Invalid choice.")
        
        elif choice == '3':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            copies = int(input("Enter number of copies: "))
            library.add_book(title, author, copies)
        
        elif choice == '6':
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "_main_":
    main()