from books import RegisterBook, BorrowBook, ReturnBook, FindBook
from members import RegisterMember, FindMember
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
library_members = []
library_books = []
def DisplayMenu():
    print("\n      Library Management System      ")
    print("-------------------------------------")
    print("1. Add a new book to the library.")
    print("2. Register a new library member.")
    print("3. Borrow a book from the library.")
    print("4. Return a book to the library.")
    print("5. Find a book in the library.")
    print("6. Find a member of the library.")
    print("7. Exit Library Management System")

def DisplayMenuTkinter():
    Menu = Tk()
    Label(Menu, text = "Library Management System").grid(column=0, row=0)
    Button(Menu, text = "Register Book", command=lambda :  RegisterBook(library_books)).grid(column=0,row=1)
    Button(Menu, text="Register Member", command=lambda : RegisterMember(library_members)).grid(column=0, row=2)
    Button(Menu, text="Borrow Book", command=lambda : BorrowBook(library_books)).grid(column=0, row=3)
    Button(Menu, text="Return Book", command=lambda : ReturnBook(library_books)).grid(column=0, row=4)
    Button(Menu, text="Find Book", command=lambda : FindBook(library_books)).grid(column=0, row=5)
    Button(Menu, text="Find Member", command=lambda : FindMember(library_members)).grid(column=0, row=6)
    Button(Menu, text="Exit Library Management System", command=Menu.destroy).grid(column=0, row=7)
    Menu.mainloop()

def main():
    DisplayMenuTkinter()

if __name__ == "__main__":
    main()