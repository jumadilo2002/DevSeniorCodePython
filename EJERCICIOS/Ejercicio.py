"""
EJERCICIO VIBE CODE - TIENDA DE CURSOS

Objetivo:
1) Entender de que trata este mini proyecto leyendo el codigo.
2) Detectar un fallo intencional.
3) Arreglarlo para que el resultado tenga sentido.

Contexto del proyecto:
Una plataforma vende cursos. Cada curso tiene precio y cupos.
Un estudiante agrega cursos a su carrito y al final paga.

Regla de negocio esperada:
- Si el estudiante compra 3 o mas cursos, debe recibir 15% de descuento.

Pista:
- El programa corre, pero el total final no coincide con la regla de negocio.
- Tu mision es encontrar el bug y corregirlo.
"""


class Curso:
    def __init__(self, nombre, precio, cupos):
        self.nombre = nombre
        self.precio = precio
        self.cupos = cupos

    def hay_cupos(self):
        return self.cupos > 0

    def reservar_cupo(self):
        if self.hay_cupos():
            self.cupos -= 1
            return True
        return False


class Carrito:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.cursos = []

    def agregar_curso(self, curso):
        if curso.reservar_cupo():
            self.cursos.append(curso)
            print(f"Curso agregado: {curso.nombre}")
        else:
            print(f"No hay cupos para: {curso.nombre}")

    def subtotal(self):
        return sum(curso.precio for curso in self.cursos)

    def total_final(self):
        total = self.subtotal()

        # FALLO INTENCIONAL: aqui hay una regla aplicada de forma incorrecta.
        # Regla correcta: si compra 3 o mas cursos, el total deberia BAJAR 15%.
        if len(self.cursos) >= 3:
            total = total * 0.85  # Aplicar descuento del 15% (multiplicar por 0.85)
        return total

    def mostrar_resumen(self):
        print("\n--- RESUMEN DE COMPRA ---")
        print(f"Estudiante: {self.estudiante}")
        for i, curso in enumerate(self.cursos, start=1):
            print(f"{i}. {curso.nombre} - ${curso.precio}")
        print(f"Subtotal: ${self.subtotal()}")
        print(f"Total final: ${self.total_final()}")


# Escenario de prueba
python_basico = Curso("Python Basico", 100, 3)
poo_python = Curso("POO en Python", 120, 2)
sql_desde_cero = Curso("SQL desde Cero", 80, 1)
git_github = Curso("Git y GitHub", 90, 0)

carrito_julian = Carrito("Julian")
carrito_julian.agregar_curso(python_basico)
carrito_julian.agregar_curso(poo_python)
carrito_julian.agregar_curso(sql_desde_cero)
carrito_julian.agregar_curso(git_github)

carrito_julian.mostrar_resumen()


"""
Reto extra (opcional):
1) Crea una clase Factura con numero, fecha y total.
2) Guarda el historial de compras de cada estudiante.
3) Agrega validacion para no permitir precios negativos.
"""
