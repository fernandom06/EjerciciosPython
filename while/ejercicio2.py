# Escriba un programa que pida números enteros mientras sean cada vez más grandes.

numero=int(input("Introduce un numero: "))
numero2=int(input(f"Introduce un numero mayor que {numero}: "))
while numero2>numero:
    numero=numero2
    numero2=int(input(f"Escriba otro numero mayor que {numero}: "))