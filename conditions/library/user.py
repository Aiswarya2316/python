class User:
    def _init_(self, username, password):
        self.username = username
        self.password = password
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)