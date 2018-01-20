"""Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor."""
numero1=int(input("Introduzca el primer numero: "))
numero2=int(input("Introduzca el segundo numero: "))

if numero1>numero2:
    if (numero1 % numero2)==0:
        print(f"El {numero1} si es multiplo de {numero2}")
    else:
        print(f"El {numero1} no es multiplo de {numero2}")
else:
    if (numero2 % numero1)==0:
        print(f"El {numero2} si es multiplo de {numero1}")
    else:
        print(f"El {numero2} no es multiplo de {numero1}")