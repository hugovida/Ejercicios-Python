#ejercicio 1.3
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
suma = numero1 + numero2

if suma % 2 == 0 and suma > 1000:
    print("La suma es par y mayor que 1000.")
elif suma % 2 == 0 and suma < 1000:
    print("La suma es par y menor que 1000.")
elif suma % 2 != 0 and suma > 1000:
    print("La suma es impar y mayor que 1000.")
else:
    print("La suma es impar y menor que 1000.")

print("Resultado de la suma:", suma)