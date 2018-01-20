"""Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años
han pasado desde ese año o cuántos años faltan para llegar a ese año."""
anno_actual=int(input("Introduzca el año actual: "))
anno=int(input("Introduzca un año: "))
if anno_actual>anno:
    print(f"Han pasado {anno_actual - anno} desde el año introducido")
else:
    print(f"Quedan {anno - anno_actual} años para llegar al año introducido")