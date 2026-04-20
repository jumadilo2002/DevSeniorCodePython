"""
Escribir un programa que pida al usuario dos numeros y muestre un menu de opciones, suma, resta, multiplicacion y division.

1. suma
2. resta
3. multiplicacion
4. division
5. division entera
6. potencia
7. modulo (residuo)
8. salir

"""


# numero1 = int(input("Ingrese el numero 1: "))

# numero2 = int(input("Ingrese el numero 2: "))

menu = """
1. suma
2. resta
3. multiplicacion
4. division
5. division entera
6. potencia
7. modulo (residuo)
8. salir
"""



def suma():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    resultado = a + b
    print(f"El resultado de la suma es: {resultado}")

def resta():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    resultado = a - b
    print(f"El resultado de la resta es: {resultado}")

def multiplicacion():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    resultado = a * b
    print(f"El resultado de la multiplicacion es: {resultado}")

def division():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    try:
        resultado = a / b
    except ZeroDivisionError:
        resultado = 0  # O el valor predeterminado que necesites
        print("Error: No se puede dividir por cero.")
    print(f"El resultado de la division es: {resultado}")

def division_entera():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    resultado = a // b
    print(f"El resultado de la division_entera es: {resultado}")

def potencia():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    resultado = a ** b
    print(f"El resultado de la potencia es: {resultado}")

def modulo():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    resultado = a % b
    print(f"El resultado del modulo es: {resultado}")


opcion = 0 

while opcion != 8:
    print(menu)
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        suma()
    elif opcion == 2:
        resta()
    elif opcion == 3:
        multiplicacion()
    elif opcion == 4:
        division()
    elif opcion == 5:
        division_entera()
    elif opcion == 6:
        potencia()
    elif opcion == 7:
        modulo()
    elif opcion == 8:
        print("gracias por usar la calculadora super 3000")
        break
    else:
        print("opcion no valida")
        


