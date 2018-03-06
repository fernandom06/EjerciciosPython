# Escriba un programa que pida dos números enteros. El programa pedirá de nuevo el segundo número mientras
# no sea mayor que el primero. El programa terminará escribiendo los dos números.

numero1=int(input("Introduce un numero: "))
numero2=int(input(f"Introduce un numero mayor que {numero1}: "))
while numero2<numero1:
    print(f"{numero2} no es mayor que {numero1}")
    numero2 = int(input(f"Introduce un numero mayor que {numero1}: "))
print(numero1,numero2)