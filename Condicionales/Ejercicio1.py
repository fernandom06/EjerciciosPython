#Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no.
print("DIVISOR DE NÚMEROS")
dividendo = int(input("Escriba el dividendo: "))
divisor = int(input("Escriba el divisor: "))

if dividendo % divisor == 0:
    print(f"La división es exacta. Cociente: {dividendo // divisor}")
else:
    print(f"La división no es exacta. Cociente: {dividendo // divisor} "
          f"Resto: {dividendo % divisor}")