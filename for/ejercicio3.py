# Escriba un programa que pregunte cuantos números se van a introducir,
#  pida esos números (que puedan ser decimales) y calcule su suma.

contador=int(input("Introduzca la cantidad de numeros que va a introducir: "))
suma=0
for i in range(contador):
    numero = float(input(f"Introduzca el numero {i+1}: "))
    suma+=numero
print(f"La suma total es de: {suma}")