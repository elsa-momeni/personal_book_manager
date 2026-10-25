from books import display_books, save_books, load_books

name = input("whats your name? ")
print("welcome", name)

book_name = input("whats your book name? ")
print("It is a good book", book_name)

books = load_books()
book_count = int(input("How many books do you want to add ? "))


for i in range(book_count):
    book = input(f"Enter the name of book {i + 1}: ")
    books.append(book)

save_books(books)
display_books(books)