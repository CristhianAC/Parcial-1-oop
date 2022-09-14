from array import array


class Library:
    def __init__(self, books : array ) -> None:
        self.books = books
    def erase(self):
        pass
    def printbooks(self):
        print("Los libros disponibles son:")
        for i in range (len(self.books)):
            print(self.books[i])

class User:
    def __init__(self, name:str) -> None:
        self.name = name
    def ask(self, bookSolicitude:str, library: Library):
        for i in range (len(library.books)-1):
            if (bookSolicitude == library.books[i]):
                library.books.remove(library.books[i])
            
    
    