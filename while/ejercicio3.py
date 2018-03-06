# Escriba un programa que pida números mientras no se escriba un número negativo. El programa terminará escribiendo
# la suma de los números introducidos.
numero=int(input("Introduce un numero: "))
numero2=int(input("introduzca otro numero: "))
suma=0
if numero2<0 or numero<0:
    print("No son positivos")
else:
    suma=numero
    while numero2>0:
        suma+=numero2
        numero2=int(input("Introduce otro numero: "))
print(f"La suma de los numeros positivos es de {suma}")