def convertir_calificacion():
    calificacion = float(input("Ingresa una calificacion de 0 a 100: "))

    if calificacion >= 90 and calificacion <= 100:
        print("Calificacion: A")
    elif calificacion >= 80:
        print("Calificacion: B")
    elif calificacion >= 70:
        print("Calificacion: C")
    elif calificacion >= 60:
        print("Calificacion: D")
    elif calificacion >= 0:
        print("Calificacion: F")
    else:
        print("Calificacion invalida")


convertir_calificacion()