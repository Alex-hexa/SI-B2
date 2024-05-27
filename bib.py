class Book:
    def __init__(self, author, title, content):
        self._author = author
        self._title = title
        self._content = content

library = []

def create():
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    content = input("Enter the content: ")
    new_book = Book(author, title, content)
    library.append(new_book)  # Add the new book to the library
    print("Book created successfully")

def update():
    title = input("Enter a title: ")
    for book in library:
        if book._title == title:
            author = input("Enter the author: ")
            content = input("Enter the content: ")
            book._author = author
            book._content = content
            print("Book updated successfully")
            break
    else:
        print("Book not found")

def read():
    title = input("Enter a title: ")
    for book in library:
        if book._title == title:
            print("Author:", book._author)
            print("Content:", book._content)
            break
    else:
        print("Book not found")

def delete():
    title = input("Enter a title: ")
    for book in library:
        if book._title == title:
            library.remove(book)
            print("Book deleted successfully")
            break
    else:
        print("Book not found")

if __name__ == "__main__":
    while True:
        command = input("Enter a command (create, update, read, delete, exit): ").strip().lower()
        if command == "create":
            create()
        elif command == "update":
            update()
        elif command == "read":
            read()
        elif command == "delete":
            delete()
        elif command == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid command")
