library_books = []

def AddBook(library_books):
    NewBookName = input("What is the name of the new book? Input it here:")
    NewAuthorName = input("What is the name of the new books author? Input it here:")
    newbook = {NewBookName : "BookName" , NewAuthorName : "NewAuthorName" , "Avaliable" : "True"}
    library_books.append(newbook)
    return(library_books)

def BorrowBook(library_books):
    Book = input("Enter the name of the book here:")
    currentindex = -1
    for i in library_books:
        currentindex += 1
        if Book in i:
            library_books[currentindex]["Avaliable"] = "False"

def ReturnBook(library_books):
    Book = input("Enter the name of the book here:")
    currentindex = -1
    for i in library_books:
        currentindex += 1
        if Book in i:
            library_books[currentindex]["Avaliable"] = "True"
def FindBook(library_books):
    Book = input("Enter the name of the book here:")
    for i in library_books:
        if Book in i:
            print(i)