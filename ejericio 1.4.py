#ejericio 1.4
edad_humana = int(input("Ingrese la edad humana: "))

if edad_humana < 0 or edad_humana > 110:
    print("Edad incorrecta.")
else:
    if edad_humana < 2:
        print("El perro no tiene edad adulta.")
    else:
        edad_perro = 2 * (edad_humana - 2) + 21
        print("Edad humana:", edad_humana)
        print("Edad del perro:", edad_perro)