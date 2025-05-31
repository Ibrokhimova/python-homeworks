
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} has already borrowed 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{book.title}' is already borrowed.")
        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)

    def __str__(self):
        return f"Member: {self.name}, Borrowed: {[book.title for book in self.borrowed_books]}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book titled '{title}' not found in library.")

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print(f"Member '{member_name}' not found.")
            return
        book = self.find_book(book_title)
        member.borrow_book(book)
        print(f"{member.name} borrowed '{book.title}'.")

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print(f"Member '{member_name}' not found.")
            return
        book = self.find_book(book_title)
        member.return_book(book)
        print(f"{member.name} returned '{book.title}'.")

if __name__ == "__main__":
    library = Library()


    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book4 = Book("Moby Dick", "Herman Melville")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)


    alice = Member("Alice")
    bob = Member("Bob")

    library.add_member(alice)
    library.add_member(bob)

    try:
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "To Kill a Mockingbird")
        library.borrow_book("Alice", "The Great Gatsby")
        library.borrow_book("Alice", "Moby Dick")
    except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
        print("Exception:", e)

    library.return_book("Alice", "1984")

    try:
        library.borrow_book("Bob", "To Kill a Mockingbird")
    except Exception as e:
        print("Exception:", e)
    try:
        library.borrow_book("Bob", "1984")
    except Exception as e:
        print("Exception:", e)

    try:
        library.borrow_book("Bob", "Unknown Book")
    except Exception as e:
        print("Exception:", e)

    print("\nLibrary Members and Borrowed Books:")
    for member in library.members:
        print(member)

    print("\nLibrary Books:")
    for book in library.books:
        print(book)
