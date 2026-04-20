# QUE ES UNA CLASE Y COMO SE DEFINE:
# Una clase en python es COMO UN MOLDE de pastel: DEFINE LA FORMA Y ESTRUCTURA.
# Con ese molde, podemos crear multiples pasteles (OBJETOS), cada uno con sus propios valores.
# En Python, se declara con la palabra reservada "class", el nombre con primera letra mayuscula y dos puntos.

# class Libro:
#     pass

# SELF, METODOS CONSTRUCTORES -- Como usar el self y el metodo constructor init?

# Dentro de una clase, las funciones se llaman METODOS. el METODO constructor INIT recibe los parametros iniciales y SIEMPRE incluye SELF, que referencia al propio objeto.
# No retorna valor: solo inicializa atributos del objeto con self

# class Libro:
#     def __init__(self, titulo, autor,fecha):
#         self.titulo = titulo            #Es un atributo del objeto (una "cajita" que queda guardad dentro de esa instancia) /  es el parametro que llega al metodo init (el valor que pasaste al creaer el objeto)
#         self.autor = autor
#         self.fecha = fecha


# Como instanciar y acceder a atributos?
# Crea variables en minuscula para instancias y para los argumentos esperados por init. Nota que self no se pasa el instanciar: pyuthon lo maneja automaticamente.

# mi_libro = Libro('cien años de soledad', 'Gabriel Garcia','20 de septiembre')
# otro_libro = Libro('El principito', 'Antoine de Saint-Expery','18 de enero del 1954')

# print(mi_libro.titulo)
# print(f"el mejor libro de mio fue: {mi_libro.titulo}")
# print(mi_libro.fecha)
# print(otro_libro.titulo)
# print(otro_libro.autor)
# print(otro_libro.fecha)

# como extender la clase libro y PRACTICA

# para afianzar, agrega nuevos parametros y crea una lista tipo catalogo. luego, recorrela con un for para imprimir cada libro. Esto solidica los conceptos de atributo, listas y bucles.


class Libro:
    def __init__(self, titulo, autor, fecha, isbn, disponible):
        self.titulo = titulo  # Es un atributo del objeto (una "cajita" que queda guardad dentro de esa instancia) /  es el parametro que llega al metodo init (el valor que pasaste al creaer el objeto)
        self.autor = autor
        self.fecha = fecha
        self.isbn = isbn
        self.disponible = disponible

#Como crear un catologo y recorrelo con FOR

catalogo = [
    Libro('cien años de soledad','Gabriel Garcia','20 de marzo','13516564652165',True),
    Libro('Proyecto de vida','jorge duque linares','13 de julio','6876546565248',False),
    Libro('Inteligencia emocional','coleman','10 de diciembre', '5416859676648', True)
]

for i in catalogo:
    print(f"titulo: {i.titulo}, autor: {i.autor}, ISBN: {i.isbn}, disponibilidad: {i.disponible}")