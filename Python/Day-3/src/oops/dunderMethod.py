class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"

    def __len__(self):
        return len(self.title)

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

    def __add__(self, other):
        if isinstance(other, Book):
            return self.price + other.price
        return self.price + other

if __name__ == "__main__":
    book1 = Book("Python Programming", "John Smith", 29.99)
    book2 = Book("Python Programming", "John Smith", 29.99)

    # Testing dunder methods
    print(str(book1))  # __str__
    print(repr(book1))  # __repr__
    print(len(book1))  # __len__
    print(book1 == book2)  # __eq__
    print(book1 + book2)  # __add__