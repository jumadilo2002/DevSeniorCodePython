



#no recibe nada y no devuelve nada

def suma1():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    resultado = a + b
    print(f"El resultado de la suma es: {resultado}")


#recibe parametros y no devuelve nada

def suma2(a,b):
    resultado = a + b
    print(f"El resultado de la suma es: {resultado}")

print("hola mundo")
#suma1()
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
suma2(n1,n2)

#no recibe parámetros pero devuelve un valor
def suma3():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    resultado = a + b
    return resultado

print(suma3())

#recibe parámetros y devuelve un valor
def suma4(a,b):
    resultado = a + b
    return resultado

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
print(suma4(n1, n2))