import os
from datetime import datetime

ARCHIVO = "usuarios.txt"


def verificar_duplicado(nombre_buscar):
    """Verifica si un nombre ya existe en el archivo."""
    if not os.path.exists(ARCHIVO):
        return False
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                if partes[0].strip().lower() == nombre_buscar.strip().lower():
                    return True
    except Exception:
        pass
    return False


def registrar_usuario():
    try:
        nombre = input("Ingrese el nombre del usuario: ").strip()
        if nombre == "":
            print("⚠️ El nombre no puede estar vacío.")
            return

        if verificar_duplicado(nombre):
            print("⚠️ Error: Ya existe un usuario registrado con ese nombre.")
            return

        edad_str = input("Ingrese la edad del usuario: ")
        if not edad_str.lstrip("-").isdigit():
            print("⚠️ La edad debe de ser numérica.")
            return

        edad = int(edad_str)
        if edad < 0:
            print("⚠️ La edad no puede ser negativa.")
            return

        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{edad},{fecha_hora}\n")

        print("✅ Usuario registrado exitosamente.")

    except PermissionError:
        print("❌ No se tienen permisos para escribir en el archivo.")
    except Exception as error:
        print(f"❌ Ocurrió un error inesperado: {error}")


def mostrar_usuarios():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print("No hay usuarios registrados.")
                return

            print("\n--- Usuarios registrados ---")
            for i, linea in enumerate(lineas, 1):
                partes = linea.strip().split(",")

                if len(partes) < 2:
                    print(f"⚠️ Línea {i} con formato incorrecto: {linea.strip()}")
                    continue

                nombre = partes[0]
                edad = partes[1]
                fecha = partes[2] if len(partes) > 2 else "Sin fecha registrada"

                print(f"Nombre: {nombre} | Edad: {edad} | Registro: {fecha}")

    except FileNotFoundError:
        print("⚠️ No se encontró el archivo de usuarios. (Aún no hay registros)")
    except PermissionError:
        print("❌ No se tienen permisos para leer el archivo.")
    except Exception as error:
        print(f"❌ Ocurrió un error inesperado: {error}")


def buscar_usuario():
    nombre_buscado = input("Ingrese el nombre exacto a buscar: ").strip().lower()
    encontrado = False

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                if partes and partes[0].lower() == nombre_buscado:
                    fecha = partes[2] if len(partes) > 2 else "N/A"
                    print("\n✅ Usuario encontrado:")
                    print(f"Nombre: {partes[0]}, Edad: {partes[1]}, Fecha: {fecha}")
                    encontrado = True
                    break
        if not encontrado:
            print("⚠️ No se encontró ningún usuario con ese nombre.")
    except FileNotFoundError:
        print("⚠️ No hay usuarios registrados aún.")


def procesar_archivo_errores():
    archivo_entrada = input(
        "Ingrese el nombre del archivo a evaluar (ej. entrada.txt): "
    )

    try:
        with open(archivo_entrada, "r", encoding="utf-8") as f_in, open(
            "usuarios_validos.txt", "w", encoding="utf-8"
        ) as f_validos, open("errores.txt", "w", encoding="utf-8") as f_errores:

            for linea in f_in:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue

                partes = linea_limpia.split(",")
                error_motivo = ""

                if len(partes) < 2:
                    error_motivo = "Faltan datos"
                else:
                    nombre = partes[0].strip()
                    edad_str = partes[1].strip()

                    if nombre == "":
                        error_motivo = "Nombre vacío"
                    elif not edad_str.lstrip("-").isdigit():
                        error_motivo = "Edad no numérica"
                    elif int(edad_str) < 0:
                        error_motivo = "Edad negativa"

                if error_motivo:
                    f_errores.write(f"{linea_limpia} ({error_motivo})\n")
                else:
                    f_validos.write(f"{linea_limpia}\n")

        print(
            "✅ Procesamiento completado. Revisa 'usuarios_validos.txt' y 'errores.txt'."
        )

    except FileNotFoundError:
        print(f"❌ No se encontró el archivo '{archivo_entrada}'.")
    except Exception as error:
        print(f"❌ Error al procesar: {error}")


def opcionales():
    print("\n--- Opciones Extra ---")
    print("1. Contar usuarios")
    print("2. Calcular edad promedio")
    print("3. Eliminar un usuario")
    print("4. Ordenar la lista de usuarios")

    sub = input("Seleccione: ")
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas_crudas = archivo.readlines()
            # Filtrar solo las líneas que tienen el formato correcto para estadísticas
            lineas_validas = [
                linea for linea in lineas_crudas if len(linea.strip().split(",")) >= 2
            ]

        if not lineas_crudas:
            print("⚠️ No hay usuarios registrados para realizar esta acción.")
            return

        if sub == "1":
            print(f"📊 Total de usuarios registrados: {len(lineas_validas)}")

        elif sub == "2":
            edades = [
                int(linea.strip().split(",")[1])
                for linea in lineas_validas
                if linea.strip().split(",")[1].lstrip("-").isdigit()
            ]
            promedio = sum(edades) / len(edades) if edades else 0
            print(f"📈 La edad promedio es: {promedio:.1f} años")

        elif sub == "3":
            nombre_eliminar = (
                input("Ingrese el nombre exacto del usuario a eliminar: ")
                .strip()
                .lower()
            )
            lineas_restantes = []
            eliminado = False

            for linea in lineas_crudas:
                partes = linea.strip().split(",")
                if partes and partes[0].strip().lower() == nombre_eliminar:
                    eliminado = True
                else:
                    lineas_restantes.append(linea)

            if eliminado:
                with open(ARCHIVO, "w", encoding="utf-8") as archivo:
                    archivo.writelines(lineas_restantes)
                print("✅ Usuario eliminado correctamente.")
            else:
                print("⚠️ No se encontró ningún usuario con ese nombre.")

        elif sub == "4":
            criterio = input("¿Ordenar por (1) Nombre o (2) Edad?: ")
            datos = []
            for linea in lineas_validas:
                partes = linea.strip().split(",")
                nombre = partes[0].strip()
                edad = partes[1].strip()
                fecha = partes[2] if len(partes) > 2 else "N/A"
                if edad.lstrip("-").isdigit():
                    datos.append((nombre, int(edad), fecha))

            if criterio == "1":
                # Ordenar alfabéticamente por el índice 0 (nombre)
                datos_ordenados = sorted(datos, key=lambda x: x[0].lower())
            elif criterio == "2":
                # Ordenar numéricamente por el índice 1 (edad)
                datos_ordenados = sorted(datos, key=lambda x: x[1])
            else:
                print("⚠️ Opción no válida.")
                return

            print("\n--- Usuarios Ordenados ---")
            for u in datos_ordenados:
                print(f"Nombre: {u[0]} | Edad: {u[1]} | Registro: {u[2]}")

    except FileNotFoundError:
        print("⚠️ No hay datos registrados.")


def menu():
    opcion = ""
    while opcion != "6":
        print("\n==== SISTEMA DE USUARIOS ====")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Buscar usuario")
        print("4. Procesar archivo del profesor (Separar válidos/errores)")
        print("5. Retos Opcionales (Contar, Promedio, Eliminar, Ordenar)")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            buscar_usuario()
        elif opcion == "4":
            procesar_archivo_errores()
        elif opcion == "5":
            opcionales()
        elif opcion == "6":
            print("Programa finalizado. ¡Éxitos con tu entrega!")
        else:
            print("⚠️ Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
