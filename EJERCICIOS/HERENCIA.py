"""
Crear una clase(Padre) Vehiculo y tres clases hijas
carro, moto, barco
"""


class Vehiculo:  # creo esta clase padre para definir los atributos comunes a todos los vehiculos
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año


class Carro(Vehiculo):  # Creo esta clase hija que hereda de vehiculo, y le agrego un atributo nuevo
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)  # Llamo al metodo constructor de la clase padre para inicializar los atributos heredados
        self.puertas = puertas  # Agrego el nuevo atributo puertas


class Moto(Vehiculo):  # Creo esta clase hija que hereda de vehiculo, y le agrego un atributo nuevo
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)  # Llamo al metodo constructor de la clase padre para inicializar los atributos heredados
        self.tipo = (tipo)  # Agrego el nuevo atributo tipo (puede ser deportiva, cruiser, etc))


class Barco(Vehiculo):  # Creo esta clase hija que hereda de vehiculo, y le agrego un atributo nuevo
    def __init__(self, marca, modelo, año, es_velero):
        super().__init__(marca, modelo, año)  # Llamo al metodo constructor de la clase padre para inicializar los atributos heredados
        self.es_velero = es_velero  # Agrego el nuevo atributo es_velero (booleano que indica si el barco es un velero o no)


# Creo instancias de cada clase hija para probar que todo funciona correctamente
carro1 = Carro("Toyota", "Corolla", 2020, 4)
moto1 = Moto("Honda", "CBR500R", 2019, "deportiva")
barco1 = Barco("Yamaha", "242X", 2021, False)
print(f"Carro: {carro1.marca} {carro1.modelo} {carro1.año} con {carro1.puertas} puertas")
print(f"Moto: {moto1.marca} {moto1.modelo} {moto1.año} tipo {moto1.tipo}")
print(f"Barco: {barco1.marca} {barco1.modelo} {barco1.año} es velero: {barco1.es_velero}")
