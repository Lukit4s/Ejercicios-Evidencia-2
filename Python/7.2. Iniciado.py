#Ejercicio 1, pedir al usuario que ingrese 10 nombres de personas
def pedir_nombres_crear_lista(cantidad_nombres):
    nombres_lista = []
    for i in range(cantidad_nombres):
        nombre = input(f"Ingrese el nombre {i + 1}: ")
        nombres_lista.append(nombre)
    return nombres_lista

def mostrar_nombres(nombres_ingresados):
    print("Los nombres ingresados son:")
    for nombre in nombres_ingresados:
        print(nombre)

nombres_ingresados = pedir_nombres_crear_lista(10)

mostrar_nombres(nombres_ingresados)

#Ejercicio 2, eliminar la tercer y la última persona de la lista
def eliminar_tercera_y_ultima_persona(nombres):
    del nombres[2]  
    del nombres[-1]  
    nombres.sort()  

eliminar_tercera_y_ultima_persona(nombres_ingresados)

mostrar_nombres(nombres_ingresados)

#Ejercicio 3
def pedir_datos_persona():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    dni = input("Ingrese el DNI: ")
    email = input("Ingrese el email: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (formato dd/mm/aaaa): ")
    return {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "email": email,
        "Fecha de nacimiento": fecha_nacimiento
    }

datos_persona = pedir_datos_persona()

print("Los datos de la persona son:")
for clave, valor in datos_persona.items():
    print(f"{clave}: {valor}")
