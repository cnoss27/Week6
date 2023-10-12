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

def DisplayBookMenu():
    BookMenu = Tk()
    Label(BookMenu, text="Book Management System").grid(column=0, row=0)
    Label(BookMenu, text="Enter Title of Book Below (If Applicable):").grid(column=0, row=1)
    inputted_book_title = Entry(BookMenu)
    inputted_book_title.grid(column=0, row=2)
    Label(BookMenu, text="Enter Name of Author Below (If Applicable):").grid(column=0, row=3)
    inputted_author_name = Entry(BookMenu)
    inputted_author_name.grid(column=0, row=4)
    Button(BookMenu, text="Register Book (Title & Author)", command=lambda: RegisterBook(library_books, inputted_book_title, inputted_author_name)).grid(column=0, row=5)
    Button(BookMenu, text="Borrow Book (Title)", command=lambda: BorrowBook(library_books, inputted_book_title)).grid(column=0, row=6)
    Button(BookMenu, text="Return Book (Title)", command=lambda: ReturnBook(library_books, inputted_book_title)).grid(column=0, row=7)
    Button(BookMenu, text="Find Book (Title)", command=lambda: FindBook(library_books, inputted_book_title)).grid(column=0, row=8)
    Button(BookMenu, text="Return To Management System", command=BookMenu.destroy).grid(column=0, row=9)
    BookMenu.mainloop()

def DisplayMemberMenu():
    MemberMenu = Tk()
    Label(MemberMenu, text="Member Management System").grid(column=0, row=0)
    Label(MemberMenu, text="Enter Member Of Interest Here:").grid(column=0, row=1)
    inputted_member_name = Entry(MemberMenu)
    inputted_member_name.grid(column=0, row=2)
    Button(MemberMenu, text="Register Member", command=lambda: RegisterMember(library_members, inputted_member_name)).grid(column=0, row=3)
    Button(MemberMenu, text="Find Member", command=lambda: FindMember(library_members, inputted_member_name)).grid(column=0, row=4)
    Button(MemberMenu, text="Return To Library Management System", command=MemberMenu.destroy).grid(column=0, row=5)
    MemberMenu.mainloop()

def DisplayMenuTkinter():
    MainMenu = Tk()
    Label(MainMenu, text = "Library Management System").grid(column=0, row=0)
    Button(MainMenu, text="Access Book Menu", command=lambda : DisplayBookMenu()).grid(column=0, row=3)
    Button(MainMenu, text="Access Member Menu", command=lambda : DisplayMemberMenu()).grid(column=0, row=6)
    Button(MainMenu, text="Exit Library Management System", command=MainMenu.destroy).grid(column=0, row=7)
    MainMenu.mainloop()

def main():
    DisplayMenuTkinter()

if __name__ == "__main__":
    main()