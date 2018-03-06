# Escriba un programa que permita crear una lista de palabras y que, a continuación,
# pida dos palabras y sustituya la primera por la segunda en la lista.

numero=int(input("Introduce el numero de palabras que tendra la lista: "))
lista=[]
for i in range(numero):
    lista.append(input(f"Introduce la palabra numero {i+1}: "))
buscar=input("Palabra que quiere sustituir: ")
sustituir=input("palabra sustituta: ")
print(lista)
for i in range(numero):
    if lista[i]==buscar:
        lista[i]=sustituir
print(lista)