class Persona:
    def __init__(selft, nombre):
        self.__name = nombre  # hago el atributo privado al ponerle las dos lineas abajo

    # mancito = Persona("carlos")
    # print(mancito.__name)    #me genera error porque es un atributo privado

    def get_name(
        self,
    ):  # creo un metodo para poder acceder al atributo privado en este caso es un metodo getter...el metodo getter es un metodo que se utiliza para obtener el valor de un atributo privado
        return self.__name  # creo un metodo para poder acceder al atributo privado

    def set_nombre(self, nombre):
        self.__name = nombre  # creo un metodo para poder modificar el valor de un atributo privado en este caso es un metodo setter...el metodo setter es un metodo que se utiliza para modificar el valor de un atributo privado


persona1 = Persona("carlos")
print(persona1.get_name())  # me imprime el nombre de la persona1 que es carlos
persona1.set_nombre("juan")  # modifico el nombre de la persona1 a juan
print(persona1.get_name())  # me imprime el nombre de la persona1 que es juan

p1 = Persona("Maria")  # creo una nueva persona llamada Maria
# print(p1.name) #me genera error porque el atributo name es privado
print(p1.get_name())  # me imprime el nombre de la persona p1 que es Maria
