#ejercicio 6
litros_menor = int(input("Ingrese el número de contenedores de menos de un litro: "))
litros_mayor = int(input("Ingrese el número de contenedores de un litro o más: "))

reembolso = (litros_menor * 0.10) + (litros_mayor * 0.25)

print("El reembolso total es:", reembolso)