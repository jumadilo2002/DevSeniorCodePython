from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

c = Cuadrado(7)
print(c.area())

class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class Desarrollador(Empleado):
    def __init__(self, salario_base):
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base * 1.2  # Ejemplo de cálculo de salario con un aumento del 20%

desarrolador = Desarrollador(5000)
print(desarrolador.calcular_salario())


