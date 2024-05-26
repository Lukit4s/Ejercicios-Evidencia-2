Mcuadrados= 2000
print("¿Cuanto mide la pared que desea pintar?")
ancho=float(input("Ingrese el ancho de la pared: "))
alto=float(input("Ingrese el alto de la pared: "))

pared= ancho * alto
costo = pared * Mcuadrados

print(f"Pintar la pared tendria un costo de: {costo} pesos")
