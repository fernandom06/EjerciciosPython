# Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los elementos repetidos
#  (dejando únicamente el primero de los elementos repetidos).

numero=int(input("Introduce el numero de palabras que tendra la lista: "))
lista=[]
for i in range(numero):
    lista.append(input(f"Introduce la palabra numero {i+1}: "))
for i in range(numero-1,-1,-1):
    if lista[i] in lista[:i]:
        del(lista[i])
print(lista[:])
