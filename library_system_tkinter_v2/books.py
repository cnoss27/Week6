library_books = []
from tkinter import *
from tkinter import messagebox
def RegisterBook(library_books, inputted_book_title, inputted_author_name):
    newbook = {inputted_book_title.get() : "BookName", inputted_author_name.get() : "AuthorName", "Avaliable": "True"}
    library_books.append(newbook)
    messagebox.showinfo(None, f"The book {inputted_book_title.get()}, written by {inputted_author_name.get()}, has been successfully registered.")
    return library_books

def BorrowBook(library_books, inputted_book_title):
    Found = 0
    currentindex = -1
    for i in library_books:
        if inputted_book_title.get() in i:
            library_books[currentindex]["Avaliable"] = "False"
            messagebox.showinfo(None, f"{inputted_book_title.get()} has been borrowed.")
            Found = 1
            return Found
    currentindex += 1
    if Found == 0:
        messagebox.showinfo(None, "This book could not be found.")
def ReturnBook(library_books, inputted_book_title):
    Found = 0
    currentindex = -1
    for i in library_books:
        if inputted_book_title.get() in i:
            library_books[currentindex]["Avaliable"] = "True"
            messagebox.showinfo(None, f"{inputted_book_title.get()} has been returned.")
            Found = 1
            return Found
        currentindex += 1
    if Found == 0:
        messagebox.showinfo(None, "This book could not be found.")

def FindBook(library_books, inputted_book_title):
    Found=0
    for i in library_books:
        if inputted_book_title.get() in i:
            messagebox.showinfo(None, i.items())
            Found=1
            return Found
    if Found == 0:
        messagebox.showinfo(None, "This book could not be found.")