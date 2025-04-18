class Library:
    def __init__(self):
        self.nom_of_books=0
        self.books=[]

    def add_book(self,book):
        self.books.append(book)
        self.nom_of_books +=1

    def print_books(self):
        for book in self.books:
            print(book)

    def get_num_books(self):
        return self.nom_of_books
lib=Library()

def add():
    lib.add_book(input("Write a book name: "))

add()
add()

print("Books in Library: ")
lib.print_books()

print("Total number of books: ",lib.get_num_books())
    
