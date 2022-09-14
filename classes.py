from array import array
#Clase Library
class Library:
    #Metodo constructor donde se le define como atributo un array de libros llamado Books
    def __init__(self, books : array ) -> None:
        self.books = books
    #Metodo encargado de recorrer el atributo books entero y los muestra
    def printbooks(self)->None:
        print("Los libros disponibles son:")
        for i in range (len(self.books)):
            print(self.books[i])

    #Metodo que permite agregar libros
    def updateBooks(self, bookToAdd: str)->None:
        self.books.append(bookToAdd)

    #Metodo que permite eliminar un libro de la lista de libros(atributo) donde se mostrara la razón por la cual se eliminó el libro
    def modify(self, opc: int, book:str)->None:

        found= False
        if opc==1:
            txt = "Libro dañado"
        elif opc==2:
            txt= "Libro perdido"
        else:
            txt = "Motivo no registrado"
        
        for i in range (len(self.books)-1):
            if (book == self.books[i]):
                self.books.remove(self.books[i])
                found= True
        if found == True:
            print("Libro eliminado de la base de datos")
            print(f"el libro {book} no estará disponible: motivo por el cual el libro no está disponible: {txt}")
        else:
            print(f"El libro {book} no se encuentra en la base de datos")



class User:
    #Metodo constructor donde su atributo es el nombre del usuario
    def __init__(self, name:str) -> None:
        self.name = name

    #Metodo donde el usuario le solicita a la bibliotecaria una lista de libros
    def ask(self, bookSolicitude:str, library: Library)->None:
        print(f"El usuario llamada {self.name} se ha llevado el libro {bookSolicitude}")
        for i in range (len(library.books)-1):
            if (bookSolicitude == library.books[i]):
                library.books.remove(library.books[i])

    #Metodo donde el usuario regresa el libro prestado
    def returnBooks(self, book:str, library:Library) -> None:
        print(f"El usuario llamada {self.name} ha devuelto el libro {book}")
        library.books.append(book)

    #Metodo donde el usuario consulta la lista de libros a la bibliotecaria.
    def askforBooks(self, library:Library)->None:
        print(f"{self.name} pregunta: ¿Que libros hay disponible?")
        print("La bibliotecaria responde:")
        library.printbooks()
    