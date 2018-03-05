# Escriba un programa que pregunte cuántos números se van a introducir,
# pida esos números y escriba cuántos negativos ha introducido.

contador=int(input("Introduzca la cantidad de numeros que va a introducir: "))
negativo=0
for i in range(contador):
    numero=int(input(f"Introduzca el numero {i+1}: "))
    if  numero<0:
        negativo+=1
print(f"La cantidad de numeros negativos es de: {negativo}")