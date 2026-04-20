from abc import ABC, abstractmethod


# =========================
# CLASE ABSTRACTA PERSONA
# =========================
class Persona(ABC):
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_rol(self):
        pass


# =========================
# HERENCIA DESDE PERSONA
# =========================
class Veterinario(Persona):
    def __init__(self, nombre, documento, especialidad):
        super().__init__(nombre, documento)
        self.especialidad = especialidad

    def mostrar_rol(self):
        return f"Veterinario - Especialidad: {self.especialidad}"

    def atender_mascota(self, mascota):
        print(f"El veterinario {self.nombre} está atendiendo a {mascota.nombre}.")


class Recepcionista(Persona):
    def __init__(self, nombre, documento):
        super().__init__(nombre, documento)

    def mostrar_rol(self):
        return "Recepcionista"

    def registrar_cliente(self, cliente):
        print(f"Cliente {cliente.nombre} registrado correctamente.")


class Cliente(Persona):
    def __init__(self, nombre, documento, telefono):
        super().__init__(nombre, documento)
        self.telefono = telefono
        self.mascotas = []  # Agregación

    def mostrar_rol(self):
        return "Cliente"

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
        print(f"Mascota {mascota.nombre} agregada al cliente {self.nombre}.")

    def mostrar_mascotas(self):
        print(f"Mascotas de {self.nombre}:")
        if not self.mascotas:
            print("- No tiene mascotas registradas.")
            return
        for mascota in self.mascotas:
            print(f"- {mascota.nombre} ({mascota.especie})")


# =========================
# CLASE MASCOTA
# =========================
class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def mostrar_info(self):
        return (
            f"Mascota: {self.nombre} , Especie: {self.especie}, "
            f"Edad: {self.edad} años , Peso: {self.peso} kg"
        )


# =========================
# CLASE TRATAMIENTO
# =========================
class Tratamiento:
    def __init__(self, nombre, costo, duracion_dias):
        self.nombre = nombre
        self.costo = costo
        self.duracion_dias = duracion_dias

    def mostrar_tratamiento(self):
        return (
            f"Tratamiento: {self.nombre} , Costo: ${self.costo:.2f}, "
            f"Duración: {self.duracion_dias} días"
        )


# =========================
# CLASE CONSULTA
# Asociación con Mascota y Veterinario
# Composición con Tratamiento
# =========================
class Consulta:
    COSTO_BASE_CONSULTA = 50000

    def __init__(self, mascota, veterinario, motivo, diagnostico):
        self.mascota = mascota
        self.veterinario = veterinario
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.tratamientos = []  # composición

    def crear_tratamiento(self, nombre, costo, duracion_dias):
        tratamiento = Tratamiento(nombre, costo, duracion_dias)
        self.tratamientos.append(tratamiento)
        print(f"Tratamiento '{nombre}' creado dentro de la consulta.")

    def mostrar_resumen(self):
        print("\n--- RESUMEN DE CONSULTA ---")
        print(self.mascota.mostrar_info())
        print(f"Veterinario: {self.veterinario.nombre}")
        print(f"Motivo: {self.motivo}")
        print(f"Diagnóstico: {self.diagnostico}")
        print("Tratamientos:")
        if not self.tratamientos:
            print("- No hay tratamientos registrados.")
        else:
            for tratamiento in self.tratamientos:
                print(f"- {tratamiento.mostrar_tratamiento()}")

    def calcular_costo_consulta(self):
        costo_tratamientos = sum(t.costo for t in self.tratamientos)
        return self.COSTO_BASE_CONSULTA + costo_tratamientos


# =========================
# CLASE ABSTRACTA METODOPAGO
# =========================
class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass


class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago en efectivo realizado por ${monto:.2f}."


class PagoTarjeta(MetodoPago):
    def procesar_pago(self, monto):
        recargo = monto * 0.05
        total = monto + recargo
        return (
            f"Pago con tarjeta realizado. "
            f"Monto base: ${monto:.2f}, recargo: ${recargo:.2f}, total: ${total:.2f}."
        )


class PagoTransferencia(MetodoPago):
    def procesar_pago(self, monto):
        descuento = monto * 0.02
        total = monto - descuento
        return (
            f"Pago por transferencia realizado. "
            f"Monto base: ${monto:.2f}, descuento: ${descuento:.2f}, total: ${total:.2f}."
        )


# =========================
# CLASE FACTURA
# Usa polimorfismo con MetodoPago
# =========================
class Factura:
    def __init__(self, consulta):
        self.consulta = consulta
        self.subtotal = consulta.calcular_costo_consulta()
        self.impuesto = 0
        self.total = 0

    def calcular_total(self):
        self.impuesto = self.subtotal * 0.19
        self.total = self.subtotal + self.impuesto
        return self.total

    def pagar(self, metodo_pago):
        if not isinstance(metodo_pago, MetodoPago):
            raise TypeError("El objeto recibido no es un método de pago válido.")

        if self.total == 0:
            self.calcular_total()

        print("\n--- FACTURA ---")
        print(f"Subtotal: ${self.subtotal:.2f}")
        print(f"Impuesto (19%): ${self.impuesto:.2f}")
        print(f"Total: ${self.total:.2f}")
        print(metodo_pago.procesar_pago(self.total))


# =========================
# PRUEBA DEL SISTEMA
# =========================
if __name__ == "__main__":
    print("=== SISTEMA DE HOSPITAL VETERINARIO ===\n")

    # Crear cliente
    cliente = Cliente("Laura Gómez", "123456789", "3001234567")
    print(cliente.mostrar_rol())

    # Crear mascotas
    mascota1 = Mascota("Max", "Perro", 5, 18.5)
    mascota2 = Mascota("Misu", "Gato", 3, 4.2)

    # Agregar mascotas al cliente
    cliente.agregar_mascota(mascota1)
    cliente.agregar_mascota(mascota2)
    cliente.mostrar_mascotas()

    # Crear veterinario
    veterinario = Veterinario("Carlos Pérez", "987654321", "Medicina interna")
    print("\n" + veterinario.mostrar_rol())

    # El veterinario atiende una mascota
    veterinario.atender_mascota(mascota1)

    # Crear consulta
    consulta = Consulta(
        mascota=mascota1,
        veterinario=veterinario,
        motivo="Falta de apetito y decaimiento",
        diagnostico="Gastritis leve",
    )

    # Crear tratamientos dentro de la consulta
    consulta.crear_tratamiento("Medicamento gástrico", 30000, 5)
    consulta.crear_tratamiento("Dieta blanda", 20000, 3)

    # Mostrar resumen
    consulta.mostrar_resumen()

    # Generar factura
    factura = Factura(consulta)
    total = factura.calcular_total()
    print(f"\nCosto total calculado: ${total:.2f}")

    # Pagar con un método
    pago1 = PagoEfectivo()
    factura.pagar(pago1)

    # Cambiar método de pago y probar nuevamente
    pago2 = PagoTarjeta()
    factura.pagar(pago2)

    # También podrías probar transferencia
    pago3 = PagoTransferencia()
    factura.pagar(pago3)
