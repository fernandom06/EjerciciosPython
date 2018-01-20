#Escriba un programa que pida dos números y que conteste cuál es el menor y cuál el mayor o que escriba que son iguales.
numero1 = int(input("Introduzca el primer numero: "))
numero2 = int(input("Introduzca el segundo numero: "))
if numero1 == numero2:
    print("Son iguales")
else:
    if numero1 > numero2:
        print(f"{numero1} es mayor que {numero2}")
    else:
        print(f"{numero2} es mayor que {numero1}")
