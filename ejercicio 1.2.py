#ejercicio 1.2
cadena = input("Ingrese una cadena de texto: ")

if cadena[-1].lower() in 'aeiou':
    print("La cadena termina en vocal.")
else:
    print("La cadena no termina en vocal.")

print("Cadena de texto:", cadena)
