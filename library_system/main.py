from books import AddBook, BorrowBook, ReturnBook, FindBook
from members import RegisterMember, FindMember
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



def main():
    while True:
        DisplayMenu()

        MenuChoice = (int(input("\nPlease choose from the above options and enter the corresponding number here:")))

        if MenuChoice == 1:
            AddBook(library_books)
        elif MenuChoice == 2:
            RegisterMember(library_members)
        elif MenuChoice == 3:
            BorrowBook(library_books)
        elif MenuChoice == 4:
            ReturnBook(library_books)
        elif MenuChoice == 5:
            FindBook(library_books)
        elif MenuChoice == 6:
            FindMember(library_members)
        elif MenuChoice == 7:
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("That is not a valid choice, please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()