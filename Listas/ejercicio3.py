# Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista
#  igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).
numero=int(input("Introduce el numero de palabras que tendra la lista: "))
lista=[]
for i in range(numero):
    lista.append(input(f"Introduce la palabra numero {i+1}: "))
print(lista[:])
lista_contraria=[]
for i in range (numero-1,-1,-1):
    lista_contraria.append(lista[i])
print(lista_contraria[:])