class Book:
    def _init_(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def _str_(self):
        return f"{self.title} by {self.author} - {self.copies} copies available"