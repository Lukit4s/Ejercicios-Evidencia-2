def main():
    nombres = []  
    while True:
        nombre = input("Ingresa un nombre (o 'fin' para terminar): ")
        if nombre.lower() == "fin":
            break  
        nombres.append(nombre)  
        
    print("\nNombres ingresados:")
    for nombre in nombres:
        print(nombre)
        
main()
