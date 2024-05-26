def tabla_multiplicar_while(numero):
    if 1 <= numero <= 10:
        i = 1
        while i <= 10:
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
            i += 1
    else:
        print("El número debe estar entre 1 y 10.")

numero_ingresado = int(input("Ingresa un número entre 1 y 10: "))
tabla_multiplicar_while(numero_ingresado)
