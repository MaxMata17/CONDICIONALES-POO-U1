edad = int(input("Ingresa tu edad: "))

if edad < 12:
    costo = 50
elif edad <= 17:
    costo = 80
else:
    costo = 120

print("El costo de entrada es: $", costo)