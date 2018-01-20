print("DIVISOR DE NÚMEROS")
dividendo = int(input("Escriba el dividendo: "))
divisor = int(input("Escriba el divisor: "))

if dividendo % divisor == 0:
    print(f"La división es exacta. Cociente: {dividendo // divisor}")
else:
    print(f"La división no es exacta. Cociente: {dividendo // divisor} "
          f"Resto: {dividendo % divisor}")