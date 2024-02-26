#ejericio 1.6
nota = float(input("Ingrese una nota (entre 1 y 7): "))

if 1 <= nota <= 7:
    if nota < 5:
        print("Suspenso")
    elif 5 <= nota < 6:
        print("Regular")
    elif 6 <= nota < 7:
        print("Bien")
else:
    print("Error: La nota debe estar entre 1 y 7.")