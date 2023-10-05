library_books = []
from tkinter import *
from tkinter import messagebox
def RegisterBook(library_books):
    BookRegMenu = Tk()

    def SubmitBook():
        newbook = {inputted_title.get(): "BookName", inputted_author.get(): "AuthorName", "Avaliable": "True"}
        library_books.append(newbook)
    Label(BookRegMenu, text="Register Book").grid(column=0, row=0)
    Label(BookRegMenu, text="Input the new book's title below:").grid(column=0, row=1)
    inputted_title = Entry(BookRegMenu)
    inputted_title.grid(column=0, row=2)
    Label(BookRegMenu, text="Input the new book's author below:").grid(column=0, row=3)
    inputted_author = Entry(BookRegMenu)
    inputted_author.grid(column=0, row=4)
    Button(BookRegMenu, text="Submit title", command = SubmitBook).grid(column=0, row=5)
    Button(BookRegMenu, text="Stop registering books", command=BookRegMenu.destroy).grid(column=0, row=6)
    BookRegMenu.mainloop()
    return library_books
def AddBook(library_books):
    NewBookName = input("What is the name of the new book? Input it here:")
    NewAuthorName = input("What is the name of the new books author? Input it here:")
    newbook = {NewBookName : "BookName" , NewAuthorName : "AuthorName" , "Avaliable" : "True"}
    library_books.append(newbook)
    return(library_books)

#def BorrowBook(library_books):
 #   Book = input("Enter the name of the book here:")
  #  currentindex = -1
   # for i in library_books:
    #    currentindex += 1
     #   if Book in i:
      #      library_books[currentindex]["Avaliable"] = "False"
def BorrowBook(library_books):
    BookBorrowMenu = Tk()

    def SubmitBook():
        Found = 0
        currentindex = -1
        for i in library_books:
            if inputted_title.get() in i:
                library_books[currentindex]["Avaliable"] = "False"
                Found = 1
                return Found
        currentindex += 1
        if Found == 0:
            messagebox.showinfo(None, "This book could not be found.")

    Label(BookBorrowMenu, text="Borrow Book").grid(column=0, row=0)
    Label(BookBorrowMenu, text="Input borrowed book's name below:").grid(column=0, row=1)
    inputted_title = Entry(BookBorrowMenu)
    inputted_title.grid(column=0, row=2)
    Button(BookBorrowMenu, text="Borrow book", command=SubmitBook).grid(column=0, row=3)
    Button(BookBorrowMenu, text="Stop borrowing books", command=BookBorrowMenu.destroy).grid(column=0, row=4)
    BookBorrowMenu.mainloop()

def ReturnBook(library_books):
    BookReturnMenu = Tk()

    def SubmitBook():
        Found = 0
        currentindex = -1
        for i in library_books:
            if inputted_title.get() in i:
                library_books[currentindex]["Avaliable"] = "True"
                Found = 1
                return Found
        currentindex += 1
        if Found == 0:
            messagebox.showinfo(None, "This book could not be found.")

    Label(BookReturnMenu, text="Return Book").grid(column=0, row=0)
    Label(BookReturnMenu, text="Input returned book's name below:").grid(column=0, row=1)
    inputted_title = Entry(BookReturnMenu)
    inputted_title.grid(column=0, row=2)
    Button(BookReturnMenu, text="Return book", command=SubmitBook).grid(column=0, row=3)
    Button(BookReturnMenu, text="Stop returning for books", command=BookReturnMenu.destroy).grid(column=0, row=4)
    BookReturnMenu.mainloop()
def FindBook(library_books):
    BookCheckMenu = Tk()

    def SubmitBook():
        Found=0
        for i in library_books:
            if inputted_title.get() in i:
                messagebox.showinfo(None, i.items())
                Found=1
                return Found
        if Found == 0:
            messagebox.showinfo(None, "This book could not be found.")
    Label(BookCheckMenu, text="Search For Book").grid(column=0, row=0)
    Label(BookCheckMenu, text="Input desired book's name below:").grid(column=0, row=1)
    inputted_title = Entry(BookCheckMenu)
    inputted_title.grid(column=0, row=2)
    Button(BookCheckMenu, text="Submit title", command = SubmitBook).grid(column=0, row=3)
    Button(BookCheckMenu, text="Stop searching for books", command=BookCheckMenu.destroy).grid(column=0, row=4)
    BookCheckMenu.mainloop()