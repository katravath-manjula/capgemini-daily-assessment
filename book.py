class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display(self):
        print(f"Book title: {self.title} \nAuthor: {self.author} \nISBN: {self.isbn}")

ob = Book("The Tale of Genji", "Vikram Seth", 65748)
ob1 = Book("One Indian Girl", "Chetan Bhagat", 56578)
ob.display()
ob1.display()
