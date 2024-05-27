class Book:
    def __init__(self, author, title, content):
        self._author = author
        self._title = title
        self._content = content

library = []

if __name__ == "__main__":

    def create(self):
        command = input("Enter a command: ")
        if command == "create":
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            content = input("Enter the content: ")
            new_book = Book(author, title, content)
            library.append(new_book)  # Add the new book to the library
            print("Book created successfully")
        else:
            print("Invalid command")

    def update(self):
        command = input("Enter a command: ")
        if command == "update":
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
        else:
            print("Invalid command")

    def read(self):
        command = input("Enter a command: ")
        if command == "update":
            title = input("Enter a title: ")
            for book in library:
                if book._title == title:
                    print(book._content)
                    break
                else:
                    print("Book not found")

    def delete(self):
        command = input("Enter a command: ")
        if command == "delete":
            title = input("Enter a title: ")
            for book in library:
                if book._title == title:
                    library.remove(book)
                    print("Book deleted successfully")
                    break
                else:
                    print("Book not found")
        else:
            print("Invalid command")