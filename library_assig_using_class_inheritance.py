class Book:
    def __init__(self,title,author,isbn,number_of_pages,price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.number_of_pages= number_of_pages
        self.price = price


    def disp_book(self):
        print(f"Title: {self.title} \n Author: {self.author} \n ISBN: {self.isbn} \n Number of Pages: {self.number_of_pages} \n Price: ${self.price}")
        

class Reference_Book(Book):
    
    def __init__(self,title,author,isbn,number_of_pages,price,dictionary):
        super().__init__(title,author,isbn,number_of_pages,price)
        self.dictionary= dictionary
    def disp_book(self):
        super().disp_book()
        print(f"Reference Book: {self.dictionary}")

   

class Fiction_Book(Book):
    def __init__(self,title,author,isbn,number_of_pages,price,genre):
        super().__init__(title,author,isbn,number_of_pages,price)
        self.genre= genre
    def disp_book(self):
        super().disp_book()
        print(f"Genre Of Book: {self.genre}\n") 


class Library:
        def __init__(self):
           self.book_library = {}

        def add_book(self,book):
           self.book_library.update({book.title:book})
           print(f"Book {book.title} added to library")

        def disp_all_books(self):
           for book in self.book_library.values():
               book.disp_book()

        def search_book_with_title(self,title):
            for book in self.book_library.values():
                if book.title.lower()==title.lower():
                    print(f"Book found with Title: {title}")
                    book.disp_book()
                    return
                
            print(f"Book not found with title: {title}")

            
        def remove_book(self,title):
            if title in self.book_library:
                self.book_library.pop(title)
                print(f"Book with title: {title} removed from the library ")
            else:
                print(f"Book Not found in the library with title: {title}")



ref=Reference_Book("Shikwa","Iqbal",'123',500,200,"Concise_Dictionary")
fict=Fiction_Book("Harry Potter","J.K Rowling","12345",100,150,"Magical Realism")

book1=Library()
book1.add_book(ref)
book1.add_book(fict)
#By calling this we displaying the both objects of Books in the library
book1.disp_all_books()
#By calling this we search book from library using title of book
book1.search_book_with_title("Shikwa")
#By calling this we remove a book from library using title of book
book1.remove_book("Harry Potter")
print("\n\n")
#After entering the search by title and remove by title the books , we will show the current books in the library
print("All Books in the library ")
book1.disp_all_books()







        

    


