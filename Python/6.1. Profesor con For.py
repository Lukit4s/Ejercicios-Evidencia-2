def tabla_multiplicar_for(numero):
    if 1 <= numero <= 10:
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
    else:
        print("El número debe estar entre 1 y 10.")

numero_ingresado = int(input("Ingresa un número entre 1 y 10: "))
tabla_multiplicar_for(numero_ingresado)
