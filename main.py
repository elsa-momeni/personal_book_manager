import os
from dotenv import load_dotenv
from books import display_books, save_books, load_books

load_dotenv()

name = input("whats your name? ")
print("welcome", name)

admin_password = os.getenv("BOOK_MANAGER_ADMIN_PASSWORD")

open_admin = input("do u want to open admin mode? yes/no: ")

if open_admin.lower == "yes":
    password = input("Enter admin password: ")
    if password == admin_password:
        print("Admin mode")
    else:
        print("wrong password")

book_name = input("whats your book name? ")
print("It is a good book", book_name)

books = load_books()
book_count = int(input("How many books do you want to add ? "))


for i in range(book_count):
    book = input(f"Enter the name of book {i + 1}: ")
    books.append(book)

save_books(books)
display_books(books)