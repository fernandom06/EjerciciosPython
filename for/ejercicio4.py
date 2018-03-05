# Escriba un programa que pida un número entero mayor que cero y calcule su factorial.

numero=int(input("Introduzca un numero mayor que cero: "))
factorial=1
for i in range(1,numero+1):
    factorial*=i
print(f"El factorial de {numero} es: {factorial}")