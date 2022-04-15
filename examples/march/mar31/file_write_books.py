#Author: Justin Chisholm
FILE_NAME = "examples/mar31/books.txt"

def write_books(books):
    try:
        with open (FILE_NAME, "w") as file:
            for book in books:
                file.write(book + "\n")
    except FileNotFoundError:
        print("Sorry, we couldn't write to the book file.")
        
def read_books():
    books = []

    try:
        with open (FILE_NAME) as file:
            for line in file:
                books.append(line.strip())
                
    except FileNotFoundError:
        print("Sorry, we couldn't read the book file")
        
    return books

def display_books(books):
    print("Book List: ")
    num = 1
    
    for book in books:
        print(f"{num}. {book}")
        num += 1
        
def add_book(books):
    #get a book from the user and add to the list
    book = input("Enter book name: ")
    books.append(book)
    print(f"{book} was successfully added to the list.")
    
    return books

def remove_book(books):
    #display book list
    display_books(books)
    
    #get book num to remove
    book_num = 0
    try:
        book_num = int(input("Enter Book Number: ")) - 1
    except ValueError: 
        print("Sorry, Invalid Number")
        return books
    
    #error check
    if book_num < 0 or book_num >= len(books):
        print("Sorry, that number is not in the range of books.")
        return books
    
    #remove book
    book = books.pop(book_num)
    print(f"{book} was removed from the list.")
    
    return books #return the list with the book removed

#main program
books = read_books()

while True:
    command = input("(V)iew, (A)dd, (D)elete, or (Q)uit: ").strip().lower()
    
    if command == "v":
        display_books(books)  
    elif command == "a":
        books = add_book(books)
    elif command == "d":
        books = remove_book(books)
    elif command == "q":
        break
    else:
        print("Invalid Command.")



print("Goodbye :(")
write_books(books)