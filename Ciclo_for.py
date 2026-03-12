#ciclo tan bonito carajo

# for x in range(1, 11):
#     print(x)

# numero = int(input("ingrese numero: "))

# for i in range(1,10+1):
#     total = numero * i
#     print(f"{numero} * {i} = {total}")

numeros = [12, 5, 8, 21, 7, 30, 4, 18, 3, 11]

mayores = 0

suma = 0

for i in numeros:
    if i > 10:
        print(i)

for i in numeros:
    if i > 10:
        mayores = mayores + 1

for i in numeros:
    if i > 10:
        suma = i + suma
print(f"la suma total de los numeros dan {suma}")

print(f"los numeros mayores de 10 son {mayores}")



