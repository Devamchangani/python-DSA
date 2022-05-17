'''
    ====== Student Library ======

    Implement a Student library System using OOPS where students can borrow a book from the list of books Create a separate 
    Library and Student class. Your program must be menu driven. You are free to choose methods and attributes of your choice
    to implement this functionality

'''

class Library:
    
    def __init__(self, listofbooks):
        self.books = listofbooks

    def displayavailablebooks(self):
        print("Books present in this library are : ")
        for book in self.books:
            print("\t  \t   \t  \t  \t" + book)

    def borrowbook(self, bookname):
        if bookname in self.books:
            print(f"You have been issude {bookname}.  Please keep it safe and return it within 30 days")
            self.books.remove(bookname)
            return True

        else:
            print("Sorry, This book has already been issued else. Please wait until the book is returned")
            return False

    def returnbook(self, bookname):   
        self.books.append(bookname)
        print("Thanks for returning this book! hope you enjoyed reding it.")


class Student:
    def reqestbook(self):
        self.book = input("Enter the books of the borrow : ")
        return self.book 

    def returnbook(self):
        self.book = input("Enter the books of the return : ")
        return self.book 


if __name__ == "__main__":
    centraLibrary = Library(["Algorithms", "Python", "Django", "Flask"])
    centraStudent = Student()
    while(True):
        Welcoming = '''
        ===== Welcome to Central library =====

        Please choose an option:
        1. List all the option
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(Welcoming)
        a = int(input("Enter a choice: "))
        if a==1:
            centraLibrary.displayavailablebooks()
        elif a==2:
            centraLibrary.borrowbook(centraStudent.reqestbook())
        elif a==3:
            centraLibrary.returnbook(centraStudent.returnbook())
        elif a==4:  
            print("Thanks for choosing central library! Have a great day ahead")
            exit()
        else:
            print("Invalide choice")  

        
