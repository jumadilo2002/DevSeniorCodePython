#     """
#     RELACION DE ASOCIACION

#     class Cliente:
#         def __init__(self, nombre):
#             self.nombre = nombre

#     class Pedido:
#         def __init__(self, cliente):
#             self.cliente = cliente

#     c1 = Cliente("Pedro")

#     p1 = Pedido(c1)    """

# #relacion de agregacion (debil)

# class Empleado:
#     def __init__(self, nombre):
#         self.nombre = nombre

# class Restaurante:
#     def __init__(self, nombre):
#         self.nombre = []

#     def agregar_empleado(self, empleado):
#         self.nombre.append(empleado)

# e = Empleado("Roberto")

# r = Restaurante()

# r.agregar_empleado(e)

# #Relacion de composicion (fuerte)
# class plato:
#     def __init__(self, nombre, precio):
#         self.nombre = nombre
#         self.precio = precio

# class pedido:
#     def __init__ (self):
#         self.platos = []

#     def agregar_plato(self, nombre, precio):
#         plato = Plato(nombre, precio)
#         self.platos.append(plato)

# #Plato = Plato("bandeja paisa", 35000) # esto no se debe de hacer porque el plato queda huerfano, es decir, no pertenece a ningun pedido, por lo tanto se debe de crear el plato dentro del pedido para que este tenga sentido.

# Pedido = Pedido()
# Pedido.agregar_plato("bandeja paisa", 35000)
# Pedido.agregar_plato("Mojarra", 25000)

# from abc import ABC, abstractmethod

# class Empleado(ABC):
#     def __init__(self, nombre):
#         self.nombre = nombre

#     @abstractmethod
#     def calcular_salario(self):
#         pass

# class Mesero(Empleado):
#     def calcular_salario(self):
#         return 1000

# class Chef(Empleado):
#     def calcular_salario(self):
#         return 2000