#ejericio 1.7
edad = int(input("Ingrese su edad: "))
ingresos_mensuales = float(input("Ingrese sus ingresos mensuales en euros: "))

if edad > 16 and ingresos_mensuales >= 1000:
    print("Debe tributar.")
else:
    print("No tiene que tributar.")