import csv

# Step 1: Read CSV and store as list of dictionaries
def read_csv(Graceful_Tresses):
    books = []
    with open(Graceful_Tresses, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            books.append(row)
    return books

# Step 2: Get books by author
def get_books_by_author(books, author):
    return [book for book in books if book['author'].lower() == author.lower()]

# Step 3: Get book by ISBN
def get_book_by_isbn(books, isbn):
    for book in books:
        if book['ISBN'] == isbn:
            return {'title': book['title'], 'price': book['price']}
    return None

# Step 4: Get books within price range
def get_books_in_price_range(books, min_price, max_price):
    return [book for book in books if min_price <= float(book['price']) <= max_price]

# Step 5: User interface
def user_interface():
    file_name = 'graceful_tresses.csv'  
    books = read_csv(file_name)

    while True:
        print("Book Search Menu")
        print("1. Search books by author")
        print("2. Search book by ISBN")
        print("3. Search books by price range")
        print("4. Add a new book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            author_name = input("Kola: ")
            author_books = get_books_by_author(books, author_name)
            if author_books:
                print("Books by", author_name)
                for book in author_books:
                    print(book)
            else:
                print("No books found for the author.")

        elif choice == '2':
            isbn = input("Enter ISBN: ")
            book_info = get_book_by_isbn(books, isbn)
            if book_info:
                print(f"Book Title: {book_info['title']}")
                print(f"Price: {book_info['price']}")
            else:
                print("Book not found for the given ISBN.")

        elif choice == '3':
            min_price = float(input("Enter minimum price: "))
            max_price = float(input("Enter maximum price: "))
            price_books = get_books_in_price_range(books, min_price, max_price)
            if price_books:
                print("Books within the price range:")
                for book in price_books:
                    print(book)
            else:
                print("No books found within the price range.")

        elif choice == '4':
            new_book = {
                'title': input("Enter book title: "),
                'author': input("Enter author name: "),
                'ISBN': input("Enter ISBN: "),
                'price': input("Enter price: ")
            }
            with open(file_name, 'a', newline='') as csvfile:
                fieldnames = ['title', 'author', 'ISBN', 'price']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(new_book)
            print("Book added successfully.")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")
