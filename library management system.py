class Library:
    # this class holds all the functions that the library performns and defines the entire LMS.
    def __init__(self, listofBooks):
        self.books = listofBooks

    def display_Available_Books(self):
        # this will display all the books that are present in the digital library.
        print(f"\n{len(self.books)} the available books are: ")
        for book in self.books:
            print(" ♦-- " + book)
        print("\n")

    def edit_Book(self, book):
        # This method within the library class will enable the librarian to make changes to the system where necessary.
        book.title = input("Enter the new title for the book: ")
        book.author = input("Enter the new author for the book: ")
        book.publisher = input("Enter the new publisher for the book: ")
        book.ISBN = input("Enter the new ISBN for the book: ")

    def borrow_Book(self, name, bookname):
        # this will all the users to borrow books from the library.
        if bookname not in self.books:
            print(
                f"{bookname} the book is not available right now someone might have taken the book at the moment.\n")
        else:
            track.append({name: bookname})
            print("book borrowed: Thank you please handle the book with care.\n")
            self.books.remove(bookname)

    def return_Book(self, bookname):
        # this method allows students to return the books they borrowed from the library.
        print("book returned : Thank you for returning the book \n")
        self.books.append(bookname)

    def remove_Book(self, book):
        # the method allows admin to remove the books from the library.
        if book in self.books:
            self.books.remove(book)
            book.library = None
        else:
            print(f"{book.title} is not in the library's collection.")

    def add_Book(self, book):
        # the methods allows to append new books in the list during compilation.
        if book not in self.books:
            self.books.append(book)
            book.library = self
        else:
            print(f"{book.title} is already in the library's collection.")

    def donateBook(self, bookname):
        # this lets users to donate books to the library.
        print("book donated : thank you for your kind gesture.\n")
        self.books.append(bookname)

class Book:
    # hte class includes details about the books in the library that may or maynot require further processing.
    def __init__(self, title, author, publisher, ISBN):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.ISBN = ISBN
        # initialization of all the object characteristics.

    def checkout(self, patron, checkout_date, due_date):
        # this allows students to check thir desired book out of the library.
        self.checkout_status = "checked_out"
        self.patron = patron
        self.checkout_date = checkout_date
        self.due_date = due_date

    def return_Book(self, return_date):
        # allows students to return the borrowed books back to the library clearing the cache.
        self.checkout_status = "available"
        self.patron = None
        self.checkout_date = None
        self.due_date = None

        # Calculate the number of days the book was overdue
        days_overdue = (return_date - self.due_date).days
        if days_overdue > 0:
            # Charge a fine to the patron for returning the book late
            self.library.chargeFine(self.patron, days_overdue)

    def donate(self):
        # initiate the donation for the books
        self.library.add_Book(self)


class Librarian:
    # will record all the characteristics of the admin the librarian.
    def __init__(self, name):
        self.name = name

    def add_Book(self, book):
        # the functionality to add new books
        self.library.add_Book(book)

    def remove_Book(self, book):
        # the functionality to remove books from the library.
        self.library.remove_Book(book)

    def edit_Book(self, book):
        # the functionality to edit existing books in the library.
        self.library.edit_Book(book)


class Fine:
    # thsi class holds all the recrods regarding the finees that are applied to teh students by crossing the due date.
    def __init__(self, amount, due_date):
        self.amount = amount
        self.due_date = due_date
        self.payment_status = "unpaid"

    def payFine(self):
        # this will allow students who have borrowed books and are overdue to pay fines while returning the book
        self.payment_status = "paid"

    def calculateFine(self, days_overdue):
        # this methods calculates the fine to be paid by the student.
        fine_amount = 0
        if days_overdue > 0:
            fine_amount = days_overdue * 0.25  # fine of $0.25 per day overdue
        return fine_amount


class Student():
    # this class defineds the student object.
    def requestBook(self):
        # This method allows student to request for books
        print("So, you want to borrow book!")
        self.book = input("Enter name of the book you want to borrow: ")
        return self.book

    def return_Book(self):
        # this allows students to return books back to the library.
        print("So, you want to return book!")
        name = input("Enter your name: ")
        self.book = input("Enter name of the book you want to return: ")
        if {name: self.book} in track:
            track.remove({name: self.book})
        return self.book

    def donateBook(self):
        # students can donate their books to the library.
        print("Okay! you want to doante book!")
        self.book = input("Enter name of the book you want to donate: ")
        return self.book

# this is where the main progam
if __name__ == "__main__":
# the main program.
    library = Library(
        ["whyme", "needHelp", "becomeRich", "Foreign", "codeWill", "SucCess"])
    student = Student()
    track = []

    print("\t\t\t\t\t\t\t****** WELCOME TO THE LIBRARY ******\n")
    print(
        """CHOOSE WHAT YOU WANT TO DO:-\n1. List books\n2. Borrow book's\n3. Return book's\n4. Give books\n5. Find books\n6. exit  \n""")

    while (True):
        # print(track)
        try:
            usr_response = int(input("Enter your choice: "))

            if usr_response == 1:  # listing
                library.display_Available_Books()
            elif usr_response == 2:  # borrow
                library.borrow_Book(
                    input("Enter your name: "), student.requestBook())
            elif usr_response == 3:  # return
                library.return_Book(student.return_Book())
            elif usr_response == 4:  # donate
                library.donateBook(student.donateBook())
            elif usr_response == 5:  # track
                for i in track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        print(f"{book} book is taken/issued by {holder}.")
                print("\n")
                if len(track) == 0:
                    print("NO BOOKS ARE ISSUED!. \n")

            elif usr_response == 6:  # exit
                print("THANK YOU ! \n")
                exit()
            else:
                print("INVAILD INPUT! \n")
        except Exception as e:  # catch errors
            print(f"{e}---> INVALID INPUT! \n")
