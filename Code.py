class Library:
# ClientsList =[]
# LibrariansList=[]
BooksList = []
Borrowed_orderList = []
total_borrowed_books = 0
total_available_books = 0
total_borrowed_orders = 0
def __init__(self, books,clients,Librarians):
self.books = []
self.clients = []
self.Librarians = []
def get_id_no(self):
return self.id_no
def set_id_no(self, id_no):
self.id_no = id_no
def add_client(self, newclient):
self.clients.append(newclient)
def add_librarian(self, newlibrarian):
self.Librarians.append(newlibrarian)
def CheckAvailability(self, book):
print("Books present in this library are: ")
if book in self.books:
print(" Available")
else:
print("Not available currently")
def borrowBook(self, bookName,clients):
if bookName in self.books:
v=int(input("Enter your id: "))
for client in clients:
print("exists")
print(f"You have been issued {bookName}.")
self.books.remove(bookName)
return True
else:
print(
"Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
return False
def returnBook(self, bookName):
x =int(input("Enter the borrowing id"))
self.books.append(bookName)
format(Book)
print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day!")
class Borrowing_order:
Borrowing_id=0
__date=3
__client_id=0
__book_id=0
__status=""
def getBorrowing_id(self,Borrowing_id):
return self.Borrowing_id
class Book:
book_id=0
__title=""
__description=""
__author =""
__status=""
def __init__(self,book_id,title,description,author,status):
self.book_id=book_id
self.title=title
self.description=description
self.author=author
self.status=status
bookslist=["python", "c","java",...]
book1 = Book(1,"Python","python programming language","M.K","Active")
book2 = Book(2,"C","C programming language","L.Z","Inactive")
book3 = Book(3,"Java","java programming language","M.J","Active")
#def borrowBook():
# pass
class Client(Library):
id=0
__full_name=""
__age=0
__id_no=0
__phone_number=0
def __init__(self, id,full_name,age,id_no,phone_number):
self.id=id
self.full_name=full_name
self.age=age
self.id_no=id_no
self.phone_number=phone_number
def get_id_no(self):
return self.id_no
def set_id_no(self,id_no):
self.id_no=id_no
def requestBook(self,book):
self.book = input("Enter the name of the book you want to borrow: ")
return self.book
def returnBook(self,book):
self.book = input("Enter the id of the book you want to return: ")
return self.book
# borrowBook("HGH",76)
class Librarian:
__id=0
__full_name = ""
__age = 0
__id_no = 0
__employment_type=""
client = Client(1,"zain malik",23,543,987643)
while(True):
welcomeMsg = '''\n*** Welcome to the Library System ***
1. Request a book
2. Return a book
3. Exit the Library
'''
print(welcomeMsg)
a = int(input("Enter a choice: "))
if a == 1:
client.requestBook("book")
print('''\n Order detalis:
client id:''',Client.id,
"book id: ", Book.book_id,
"borrowing id: ", Borrowing_order.Borrowing_id)
elif a == 2:
client.returnBook("book")
elif a == 3:
print("Thanks for choosing our Library. See you soon<3")
exit()
else:
print("Invalid Choice!")
