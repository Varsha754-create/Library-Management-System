class Book:
    def __init__(self, book_id, book_name, author, quantity):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.quantity = quantity

def add_book(book):
    file = open("books.txt", "a")
    file.write(
        f"{book.book_id},{book.book_name},{book.author},{book.quantity}\n")
    file.close()

def show_books():
    file = open("books.txt", "r")
    data = file.read()
    file.close()
    return data

def check_book_id(book_id):
    file = open("books.txt", "r")
    books = file.readlines()
    file.close()
    for book in books:
        data = book.strip().split(",")
        if data[0] == book_id:
            return True
    return False

def search_book(book_id):
    file = open("books.txt", "r")
    books = file.readlines()
    file.close()
    for book in books:
        data = book.strip().split(",")
        if data[0] == book_id:
            return book
    return "Book Not Found"

def delete_book(book_id):
    file = open("books.txt", "r")
    books = file.readlines()
    file.close()
    file = open("books.txt", "w")
    for book in books:
        data = book.strip().split(",")
        if data[0] != book_id:
            file.write(book)
    file.close()

def update_book(book):
    file = open("books.txt", "r")
    books = file.readlines()
    file.close()
    file = open("books.txt", "w")

    for data in books:
        record = data.strip().split(",")
        if record[0] == book.book_id:
            file.write(
                f"{book.book_id},{book.book_name},{book.author},{book.quantity}\n")
        else:
            file.write(data)
    file.close()      