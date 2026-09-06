def clasificar_triangulo():
    lado1 = float(input("Ingresa el primer lado: "))
    lado2 = float(input("Ingresa el segundo lado: "))
    lado3 = float(input("Ingresa el tercer lado: "))

    if lado1 == lado2 and lado2 == lado3:
        print("El triangulo es equilatero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triangulo es isosceles")
    else:
        print("El triangulo es escaleno")

clasificar_triangulo()