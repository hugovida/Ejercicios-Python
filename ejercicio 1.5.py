#ejercicio 1.5
mes = input("Ingrese el nombre de un mes: ").lower()

dias = None

if mes in ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"]:
    dias = 31
elif mes in ["abril", "junio", "septiembre", "noviembre"]:
    dias = 30
elif mes == "febrero":
    # Solicitar al usuario si el año es bisiesto
    es_bisiesto = input("¿Es un año bisiesto? (s/n): ").lower() == "s"
    dias = 29 if es_bisiesto else 28

if dias is not None:
    print(f"{mes.capitalize()} tiene {dias} días.")
else:
    print("Nombre de mes no válido.")