videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10,
    },
    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5,
    },
    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8,
    },
}

historial_ventas = []


def pedir_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("El valor debe ser mayor que cero.")
        except ValueError:
            print("Ingresa un número entero válido.")


def pedir_decimal_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("El valor debe ser mayor que cero.")
        except ValueError:
            print("Ingresa un número válido.")


def agregar_videojuego(videojuegos):
    print("\n=== Agregar videojuego ===")
    codigo = input("Ingrese el código del videojuego: ").strip().upper()

    if codigo in videojuegos:
        print("Ese código ya existe. No se puede agregar el videojuego.")
        return

    nombre = input("Ingrese el nombre del videojuego: ").strip()
    plataforma = input("Ingrese la plataforma: ").strip()
    precio = pedir_decimal_positivo("Ingrese el precio: ")
    cantidad = pedir_entero_positivo("Ingrese la cantidad en inventario: ")

    videojuegos[codigo] = {
        "nombre": nombre,
        "plataforma": plataforma,
        "precio": precio,
        "cantidad": cantidad,
    }
    print("Videojuego agregado correctamente.")


def mostrar_inventario(videojuegos):
    print("\n=== Inventario ===")
    if not videojuegos:
        print("No hay videojuegos registrados.")
        return

    for codigo, datos in videojuegos.items():
        print(f"Código: {codigo}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Plataforma: {datos['plataforma']}")
        print(f"Precio: ${datos['precio']:,.0f}")
        print(f"Cantidad: {datos['cantidad']}")
        print("-" * 30)


def buscar_videojuego(videojuegos):
    print("\n=== Buscar videojuego ===")
    codigo = input("Ingrese el código del videojuego: ").strip().upper()

    if codigo in videojuegos:
        datos = videojuegos[codigo]
        print(f"Código: {codigo}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Plataforma: {datos['plataforma']}")
        print(f"Precio: ${datos['precio']:,.0f}")
        print(f"Cantidad: {datos['cantidad']}")
    else:
        print("No se encontró un videojuego con ese código.")


def actualizar_precio(videojuegos):
    print("\n=== Actualizar precio ===")
    codigo = input("Ingrese el código del videojuego: ").strip().upper()

    if codigo not in videojuegos:
        print("El videojuego no existe.")
        return

    nuevo_precio = pedir_decimal_positivo("Ingrese el nuevo precio: ")
    videojuegos[codigo]["precio"] = nuevo_precio
    print("Precio actualizado correctamente.")


def registrar_venta(videojuegos):
    print("\n=== Registrar venta ===")
    codigo = input("Ingrese código del videojuego: ").strip().upper()

    if codigo not in videojuegos:
        print("El videojuego no existe.")
        return

    cantidad_vender = pedir_entero_positivo("Ingrese cantidad a vender: ")
    datos = videojuegos[codigo]

    if cantidad_vender > datos["cantidad"]:
        print("No hay inventario suficiente para realizar la venta.")
        return

    subtotal = datos["precio"] * cantidad_vender
    descuento = 0
    total = subtotal

    if subtotal > 500000:
        descuento = subtotal * 0.10
        total = subtotal - descuento

    datos["cantidad"] -= cantidad_vender

    factura = {
        "codigo": codigo,
        "nombre": datos["nombre"],
        "precio_unitario": datos["precio"],
        "cantidad": cantidad_vender,
        "subtotal": subtotal,
        "descuento": descuento,
        "total": total,
    }
    historial_ventas.append(factura)

    print("\nFactura")
    print("-------")
    print(f"Juego: {datos['nombre']}")
    print(f"Precio unitario: ${datos['precio']:,.0f}")
    print(f"Cantidad: {cantidad_vender}")
    if descuento > 0:
        print(f"Descuento: -${descuento:,.0f}")
    print(f"Total: ${total:,.0f}")


def mostrar_estadisticas(videojuegos):
    print("\n=== Estadísticas ===")
    if not videojuegos:
        print("No hay videojuegos registrados.")
        return

    total_videojuegos = len(videojuegos)
    valor_total_inventario = 0
    suma_precios = 0
    videojuego_mas_costoso = None
    videojuego_mayor_cantidad = None

    for codigo, datos in videojuegos.items():
        valor_total_inventario += datos["precio"] * datos["cantidad"]
        suma_precios += datos["precio"]

        if (
            videojuego_mas_costoso is None
            or datos["precio"] > videojuego_mas_costoso["precio"]
        ):
            videojuego_mas_costoso = {"codigo": codigo, **datos}

        if (
            videojuego_mayor_cantidad is None
            or datos["cantidad"] > videojuego_mayor_cantidad["cantidad"]
        ):
            videojuego_mayor_cantidad = {"codigo": codigo, **datos}

    promedio_precios = suma_precios / total_videojuegos

    print(f"Total de videojuegos registrados: {total_videojuegos}")
    print(f"Valor total del inventario: ${valor_total_inventario:,.0f}")
    print(
        f"Videojuego más costoso: {videojuego_mas_costoso['nombre']} "
        f"({videojuego_mas_costoso['codigo']}) - ${videojuego_mas_costoso['precio']:,.0f}"
    )
    print(
        f"Videojuego con mayor cantidad disponible: {videojuego_mayor_cantidad['nombre']} "
        f"({videojuego_mayor_cantidad['codigo']}) - {videojuego_mayor_cantidad['cantidad']} unidades"
    )
    print(f"Promedio de precios: ${promedio_precios:,.0f}")


def buscar_por_plataforma(videojuegos):
    print("\n=== Buscar por plataforma ===")
    plataforma_busqueda = input("Ingrese la plataforma a buscar: ").strip().lower()
    encontrados = False

    for codigo, datos in videojuegos.items():
        if datos["plataforma"].strip().lower() == plataforma_busqueda:
            print(f"Código: {codigo}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Plataforma: {datos['plataforma']}")
            print(f"Precio: ${datos['precio']:,.0f}")
            print(f"Cantidad: {datos['cantidad']}")
            print("-" * 30)
            encontrados = True

    if not encontrados:
        print("No se encontraron videojuegos para esa plataforma.")


def mostrar_inventario_bajo(videojuegos):
    print("\n=== Videojuegos con inventario bajo ===")
    encontrados = False

    for codigo, datos in videojuegos.items():
        if datos["cantidad"] < 3:
            print(f"Código: {codigo}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Plataforma: {datos['plataforma']}")
            print(f"Precio: ${datos['precio']:,.0f}")
            print(f"Cantidad: {datos['cantidad']}")
            print("-" * 30)
            encontrados = True

    if not encontrados:
        print("No hay videojuegos con inventario bajo.")


def mostrar_videojuego_mas_vendido(historial_ventas):
    print("\n=== Videojuego más vendido ===")
    if not historial_ventas:
        print("Aún no hay ventas registradas.")
        return

    ventas_por_videojuego = {}

    for venta in historial_ventas:
        codigo = venta["codigo"]
        ventas_por_videojuego[codigo] = (
            ventas_por_videojuego.get(codigo, 0) + venta["cantidad"]
        )

    codigo_mas_vendido = max(ventas_por_videojuego, key=ventas_por_videojuego.get)
    total_vendido = ventas_por_videojuego[codigo_mas_vendido]
    datos = videojuegos[codigo_mas_vendido]

    print(f"Código: {codigo_mas_vendido}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Plataforma: {datos['plataforma']}")
    print(f"Unidades vendidas: {total_vendido}")


def eliminar_videojuego(videojuegos):
    print("\n=== Eliminar videojuego ===")
    codigo = input("Ingrese el código del videojuego: ").strip().upper()

    if codigo in videojuegos:
        eliminado = videojuegos.pop(codigo)
        print(f"Se eliminó el videojuego: {eliminado['nombre']}")
    else:
        print("No se encontró un videojuego con ese código.")


def menu():
    while True:
        print("\n===== TIENDA DE VIDEOJUEGOS =====")
        print("1. Agregar videojuego")
        print("2. Mostrar inventario")
        print("3. Buscar videojuego por código")
        print("4. Actualizar precio")
        print("5. Registrar venta")
        print("6. Mostrar estadísticas")
        print("7. Eliminar videojuego")
        print("8. Buscar videojuegos por plataforma")
        print("9. Mostrar videojuegos con inventario bajo")
        print("10. Mostrar videojuego más vendido")
        print("11. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_videojuego(videojuegos)
        elif opcion == "2":
            mostrar_inventario(videojuegos)
        elif opcion == "3":
            buscar_videojuego(videojuegos)
        elif opcion == "4":
            actualizar_precio(videojuegos)
        elif opcion == "5":
            registrar_venta(videojuegos)
        elif opcion == "6":
            mostrar_estadisticas(videojuegos)
        elif opcion == "7":
            eliminar_videojuego(videojuegos)
        elif opcion == "8":
            buscar_por_plataforma(videojuegos)
        elif opcion == "9":
            mostrar_inventario_bajo(videojuegos)
        elif opcion == "10":
            mostrar_videojuego_mas_vendido(historial_ventas)
        elif opcion == "11":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
