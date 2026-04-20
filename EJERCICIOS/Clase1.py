class Perro:    #por lo generar el nombre de la clase empieza en mayuscula
    def __init__(self, nombre, edad):   #metodo construccion
        self.name = nombre
        self.age = edad

    def ladrar(self):
        return "!guau!"

    def rascarse(self):
        print("me estoy rascando")

perro1 = Perro("Fido",3)
perrito = Perro("Rex",5)
print(perro1.name, perro1.age)
print(perrito.name, perrito.age)
print(perro1.ladrar())
print(perrito.ladrar())
perrito.rascarse()