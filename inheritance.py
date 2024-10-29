# Managing a library system
# parent class
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display_info(self):
        return f"The Title {self.title}, author {self.author}"
    
# child class/derived class
class LibraryBook(Book):
    def __init__(self,title,author,isbn,copies_available):
        super().__init__(title,author)
        self.isbn=isbn
        self.copies_available=copies_available
    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -=1
            return f"{self.title} borrowed. Copies left: {self.copies_available}"
        else:
            return f"Number of copies available: {self.title} unavaialble"
    def return_book(self):
        self.copies_available+=1
        return f"{self.title} returned. Copies left: {self.copies_available}"
    
# usage example
book1=LibraryBook("Kifo Kisimani","Adrian Ochieng'",123456-7757-45,20)

print(book1.display_info())

print(book1.borrow_book())
print(book1.borrow_book())

print(book1.return_book())