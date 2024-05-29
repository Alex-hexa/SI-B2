import json  # Import the json module
import os  # Import the os module

# Definition de la classe Book
class Book:
    def __init__(self, tag, title, image):
        self.tag = tag
        self.title = title
        self.image = image

# Vérifie si le fichier 'library.json' existe
if not os.path.exists('library.json'):
    # Le crée s'il n'existe pas
    with open('library.json', 'w') as file:
        json.dump([], file)

# Fonction create
def create():
    title = input("Enter the title: ")
    tag = input("Enter the tag: ")
    image = input("Enter the image: ")
    new_book = Book(tag, title, image)
    with open('library.json', 'r') as file:
        library = json.load(file)
    library.append(new_book.__dict__)
    with open('library.json', 'w') as file:
        json.dump(library, file)
    print("Book created successfully")

# Fonction update
def update():
    title = input("Enter a title: ")
    with open('library.json', 'r') as file:
        library = json.load(file)
    for book in library:
        if book['title'] == title:
            tag = input("Enter the tag: ")
            image = input("Enter the image: ")
            book['tag'] = tag
            book['image'] = image
            with open('library.json', 'w') as file:
                json.dump(library, file)
            print("Book updated successfully")
            break
    else:
        print("Book not found")

# Fonction read
def read():
    title = input("Enter a title: ")
    with open('library.json', 'r') as file:
        library = json.load(file)
    for book in library:
        if book['title'] == title:
            print("Tag:", book['tag'])
            print("Image:", book['image'])
            break
    else:
        print("Book not found")

# Fonction read_all
def read_all():
    with open('library.json', 'r') as file:
        library = json.load(file)
    if not library:
        print("No books found")
    for book in library:
        print("Title:", book['title'])
        print("Tag:", book['tag'])
        print("Image:", book['image'])
        print("--------------------")

# Fonction delete
def delete():
    title = input("Enter a title: ")
    with open('library.json', 'r') as file:
        library = json.load(file)
    for book in library:
        if book['title'] == title:
            library.remove(book)
            with open('library.json', 'w') as file:
                json.dump(library, file)
            print("Book deleted successfully")
            break
    else:
        print("Book not found")

# Programme principal
if __name__ == "__main__":
    while True:
        command = input("Enter a command (create, update, read, read-all, delete, exit): ").strip().lower()
        if command == "create":
            create()
        elif command == "update":
            update()
        elif command == "read":
            read()
        elif command == "read-all":
            read_all()
        elif command == "delete":
            delete()
        elif command == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid command")
