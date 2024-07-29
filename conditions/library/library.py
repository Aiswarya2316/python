# from book import Book
# from user import User
class Library:
    def _init_(self):
        self.users = {}
        self.books = {}

    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists!")
        else:
            self.users[username] = User(username, password)
            print(f"User {username} registered successfully.")

    def login_user(self, username, password):
        if username in self.users and self.users[username].password == password:
            print(f"User {username} logged in successfully.")
            return self.users[username]
        else:
            print("Invalid username or password.")
            return None

    def add_book(self, title, author, copies):
        if title in self.books:
            self.books[title].copies += copies
        else:
            self.books[title] = Book(title, author, copies)
        print(f"Book {title} added/updated successfully.")

    def borrow_book(self, user, title):
        if title in self.books and self.books[title].copies > 0:
            self.books[title].copies -= 1
            user.borrow_book(self.books[title])
            print(f"Book {title} borrowed by {user.username}.")
        else:
            print("Book not available.")

    def return_book(self, user, title):
        if title in self.books:
            self.books[title].copies += 1
            user.return_book(self.books[title])
            print(f"Book {title} returned by {user.username}.")
        else:
            print("Invalid book title.")