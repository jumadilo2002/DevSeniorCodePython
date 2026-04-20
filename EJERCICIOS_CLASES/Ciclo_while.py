menu = """
RESTAURANTE EL BUEN SABOR
1.HAMBURGUESA - $20.000
2.PIZZA - $15.000
3.ENSALADA - $4.500
4.SALCHIPAPA - $8.000
5.PERRO CALIENTE - $12.000
6.SALIR
"""
print(menu)

total_salchipapa = 0
total_ensalada = 0
total_perro_caliente = 0
total_pizza = 0
total_hamburguesa = 0

cantidad_salchipapa = 0
cantidad_ensalada = 0
cantidad_perro_caliente = 0
cantidad_pizza = 0
cantidad_hamburguesa = 0

cantidad_total = (cantidad_salchipapa + cantidad_ensalada + cantidad_perro_caliente + cantidad_pizza + cantidad_hamburguesa)

opcion = 0
total = 0

while opcion != 6:    #while significa mientras que:
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        print("has elegido hamburguesas")
        total = total + 20000
        total_hamburguesa = total_hamburguesa + 20000
        cantidad_hamburguesa += 1
    elif opcion == 2:
        print("has eleigo Pizza")
        total = total + 15000
        total_pizza = total_pizza + 15000
        cantidad_pizza += 1 
    elif opcion == 3:
        print("has eleigo Ensalada")
        total = total + 4500
        total_ensalada = total_ensalada + 4500
        cantidad_ensalada += 1
    elif opcion == 4:
        print("has eleigo Salchipapa")
        total = total + 8000
        total_salchipapa = total_salchipapa + 8000
        cantidad_salchipapa += 1
    elif opcion == 5:
        print("has eleigo Perro caliente")
        total = total + 12000
        total_perro_caliente = total_perro_caliente + 12000
        cantidad_perro_caliente += 1 
    elif opcion == 6:
        print("Gracias por visitar el restaurante el buen sabor. hasta luego gordito")
        cantidad_total = (cantidad_salchipapa + cantidad_ensalada + cantidad_perro_caliente + cantidad_pizza + cantidad_hamburguesa)
        print(f"el total de sus productos es {total}, y la cantidad es {cantidad_total}")
        print(f" el total de hamburguesas es: {total_hamburguesa}, cantidad: {cantidad_hamburguesa}")
        print(f" el total de pizza es: {total_pizza}, cantidad: {cantidad_pizza}")
        print(f" el total de salchipapa es: {total_salchipapa}, cantidad: {cantidad_salchipapa}")
        print(f" el total de perro caliente es: {total_perro_caliente}, cantidad {cantidad_perro_caliente}")
        print(f" el total de ensaladas es: {total_ensalada}, cantidad: {cantidad_ensalada}")
        
        break
    else:
        print("Opcion no valida por favor elige una opcion valida")
        


















