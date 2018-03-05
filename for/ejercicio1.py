# Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el
#  primero hasta el segundo.

numero1=int(input("Intriduzca un numero: "))
numero2=int(input(f"Intriduzca un numero mayor o igual que {numero1}: "))

if  numero2<numero1:
    print(f"Le he pedido un numero igual o mayor que {numero1}")
else:
    for i in range(numero1,numero2):
        if i%2==0:
            print(f"{i} es Par")
        else:
            print(f"{i} es Impar")
