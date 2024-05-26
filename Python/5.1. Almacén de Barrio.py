print("Despensa de barrio, tendra un descuento de acuerdo a la cantidad que compre")
valorleche=1000
cantleches=int(input("Ingrese la cantidad de leches que desea comprar: "))
cliente=int(input("Ingrese 0 si el cliente es jubilado, ingrese 1 si no lo es: "))

if cantleches >= 24 and cliente == 1:
    descuento= cantleches - (cantleches * 0.15)
    total= descuento * valorleche
    print(f"El total a pagar con descuento es de: {total} pesos")
    
elif cantleches >= 12 and cliente == 1:
    descuento= cantleches - (cantleches * 0.10)
    total= descuento * valorleche
    print(f"El total a pagar con descuento es de: {total} pesos")
    
elif cantleches >= 24 and cliente == 0:
    descuento= cantleches - (cantleches * 0.25)
    total= descuento * valorleche
    print(f"El total a pagar con descuento es de: {total} pesos")
    
elif cantleches >= 12 and cliente == 0:
    descuento= cantleches - (cantleches * 0.20)
    total= descuento * valorleche
    print(f"El total a pagar con descuento es de: {total} pesos")
    
elif cantleches < 12 and cliente == 0:
    descuento= cantleches - (cantleches * 0.10)
    total= descuento * valorleche
    print(f"El total a pagar con descuento es de: {total} pesos")

else:
    total= valorleche * cantleches
    print(f"El total a pagar es de: {total} pesos")
