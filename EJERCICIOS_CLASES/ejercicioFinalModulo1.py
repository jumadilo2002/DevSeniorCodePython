









def registrar_estudiantes():
    nombre = (input("ingrese el nombre del estudiante: "))
    edad = int(input("ingrese la edad del estudiante: "))
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))
    #suma = nota1 + nota2 + nota3
    return nombre, edad, nota1, nota2, nota3


def promediodenotas(nota1, nota2, nota3):
    promedio = ((nota1 + nota2 + nota3)/3)
    print(f"el promedio de notas es {promedio}")
    return promedio
    

def estado_estudiante(promedio):
    if promedio < 3:
        print("reprobado")
    elif promedio > 4:
        print("Aprobado")
    elif promedio >= 3 and promedio < 4:
        print("En recuperacion")
    else:
        print("error")
    

menu = """ 
1️⃣ Registrar estudiantes
2️⃣ Calcular el promedio de tres notas
3️⃣ Determinar el estado del estudiante
4️⃣ Permitir registrar varios estudiantes usando un menú
5️⃣ Mostrar un resumen final
6. salida
"""


print(menu)

opcion = 0

nombre = None
edad = None
nota1 = None
nota2 = None
nota3 = None
promedio = None 

total_estudiantes = 0
suma_promedios = 0

registrado = False
promedio_sumado = False

while opcion != 6:
    opcion = int(input("ingrese la opcion a seleccionar: "))

    if opcion == 1:
        nombre, edad, nota1, nota2, nota3 = registrar_estudiantes()
        promedio = None
        registrado = True
        promedio_sumado = False
        total_estudiantes += 1

    elif opcion == 2:
        if registrado == True:
            promedio = promediodenotas(nota1, nota2, nota3)

            if promedio_sumado == False:
                suma_promedios += promedio
                promedio_sumado = True
        else:
            print("primero debe de registrar un estudiante.")

    elif opcion == 3:
        if promedio is not None:
            estado_estudiante(promedio)
        else: 
            print("primero debe calcular el promedio.")
    
    elif opcion == 4:
        nombre, edad, nota1, nota2, nota3 = registrar_estudiantes()
        promedio = promediodenotas(nota1, nota2, nota3)
        estado_estudiante(promedio)

        total_estudiantes += 1
        suma_promedios += promedio
        registrado = True
        promedio_sumado = True

    elif opcion == 5:
        print("===== RESUMEN FINAL =====")
        print("Total de estudiantes registrados:", total_estudiantes)

        if total_estudiantes > 0:
            if suma_promedios > 0:
                promedio_general = suma_promedios / total_estudiantes
                print("Promedio general del grupo:", promedio_general)
            else:
                print("Promedio general del grupo: 0")
        else:
            print("Promedio general del grupo: 0")

    elif opcion == 6:
        print("saliendo del programa...")
    
    else:
        print("Opcion no valida")
        
        