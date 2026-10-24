name = input("whats your name? ")
print("welcome", name)

book_name = input("whats your book name? ")
print("It is a good book", book_name)

book_count = int(input("How many books do you want to add ? "))
books = []

for i in range(book_count):
    book = input(f"Enter the name of book {i + 1}: ")
    books.append(book)
    print("Your books:")

for book in books:
    print(book)