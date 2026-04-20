
#Una clase es una plantilla o un plano para crear objetos. Define las propiedades y comportamientos que los objetos de esa clase tendran. 
#es una forma de organizar y estructurar el codigo, permitiendo la reutilizacion y la modularidad.
#explicado de forma sencilla, una clase es como un molde que define las caracteristicas y comportamientos de un objeto.

class Libro: #class es la palabra reservada para definir una clase. la primera letra de la clase se escribe en mayuscula por convencion.
    def__init__(self, titulo, autor): #el metodo__init__ es un metodo especial que se llama automaticamente cuando se crea un objeto de la clase. se utiliza para inicializar los atributos del objeto.
#basicamente lo que se hizo fue usar def para definir el metodo, init es el nombre del metodo, y los parametros entre parentesis son los atributos que se le asignaran al objeto.
        self.titulo = titulo #self es una referencia al objeto actual. se utiliza para acceder
        self.autor = autor #a los atributos y metodos de la clase. en este caso, se asigna el valor del parametro titulo al atributo titulo del objeto, y lo mismo para autor.
    
mi_libro = libro("100 anios de soledad","Gabriel Garcia Marquez") #para crear un objeto de la clase, se llama a la clase como si fuera una funcion, pasando los argumentos necesarios para el metodo__init__. en este caso, se crea un objeto llamado mi_libro con el titulo "100 anios de soledad" y el autor "Gabriel Garcia Marquez".
otro_libro = libro("el principito","saint-exupery") #se crea otro objeto llamado otro_libro con el titulo "el principito" y el autor "saint-exupery".

print(f"mi_libro: {mi_libro.titulo} {mi_libro.autor}")
print(f"otro_libro: {otro_libro.titulo} {otro_libro.autor}")

