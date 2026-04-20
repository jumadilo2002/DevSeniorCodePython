# Los metodos de instancia en python dan vida a los objetos: permiten consultar, validar y modificar su estado interno con precision.
# como aplicar self, diseñar str, y crear metodos como prestar y devolver en una clase Liubro con ISBN y campo booleano de disponibilidad, tal como se mostro al ejecutar el codigo pasado...

# Que son metodos de instancia y como usan self?
# En python, los metodos definidos dentro de una clase operan sobre cada instancia usando el parametro self. Asi, cada objeto puede interactuar con sus propios datos, como el campo booleano de disponibilida
# self referenciar la instancia actual: accede a atributos y modifica estado.
# disponible como booleano: indica si el libro se puede prestar
# catologo como lista: agrupa varios libros para iterar e imprimir sus datos con un for.

# como orgranizar el catalogo y el campo disponible?
# agregar el ISBN y el booleano disponible al inicializador
# Crea dos libros y anadelos a una lista catalogo
# recorre con for e imprime cada libro

# class Libro:
#     def __init__(self, titulo, autor, isbn, disponible=True):
#         self.titulo = titulo
#         self.autor = autor
#         self.isbn = isbn
#         self.disponible = disponible

# # CREAR LIBROS CON DATOS CON AYUDA DE NUESTRO MOLDE

# Libro1 = Libro('Juan la maravilla', 'Juan Manuel Diaz Lopez', '52465246185')
# Libro2 = Libro("Don Nestor y sus aventuras", "Nicolas Campos", "64657897652")

# catalogo = [Libro1, Libro2]

#for catalogos in catalogo:
#    print(f"LIBRO: {catalogos.titulo}, AUTOR: {catalogos.autor}, ISBN: {catalogos.isbn}, DISPONIBILIDAD: {catalogos.disponible}")

# COMO PUEDO MEJORAR LA SALIDA CON STR Y RETURN?
# EL metodo especial STR se ejecuta automaticamente al hacer print de un objeto. Debe usar self y siempre retornar un string con return. sin return, aparece un error al imprimir el objeto.


historial_prestamos = []

class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            historial_prestamos.append(self)
            return f"{self.disponible}: prestado exitosamente"

    def devolver(self):
        self.disponible = True
        return f"{self.disponible}: ha sido devuelto y disponible nuevamente"

    def es_popular(self):
        return historial_prestamos.count(self) > 5

    # def __str__(self):
    #     # retornar la presentacion escrita del libro
    #     return f"{self.titulo} - {self.autor} ! ISBN: {self.isbn} ! disponibilidad: {self.disponible}"



Libro1 = Libro('Juan la maravilla', 'Juan Manuel Diaz Lopez', '52465246185')
Libro2 = Libro("Don Nestor y sus aventuras", "Nicolas Campos", "64657897652")

print(Libro1.prestar())
print(Libro1.devolver())
print(Libro1.es_popular())




