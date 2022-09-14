from classes2Books import Library, User
panamericana = Library(books= ["HG", "HP"])
JesusDeLaCruz= User(name= "Jesus")
panamericana.printbooks()
JesusDeLaCruz.ask(bookSolicitude="HG", library=panamericana)
panamericana.printbooks()
#Terminado, faltan vainas pero aja