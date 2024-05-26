def calcular_promedio_y_rendimiento():
    
    cantidad_alumnos = int(input("Ingrese la cantidad de alumnos que rindieron el examen: "))
    total_notas = 0

    for i in range(1, cantidad_alumnos + 1):
        while True:
            try:
                nota = float(input(f"Ingrese la nota del alumno {i} (entre 0 y 10): "))
                if 0 <= nota <= 10:
                    break
                
                else:
                    print("La nota debe estar entre 0 y 10. Intente nuevamente.")
            except ValueError:
                print("Ingrese un valor numérico válido.")
                
        total_notas += nota

    promedio = total_notas / cantidad_alumnos

    if promedio > 8:
        rendimiento = "elevado"
    elif 6 <= promedio <= 8:
        rendimiento = "aceptable"
    else:
        rendimiento = "bajo"

    print(f"El promedio de notas es: {promedio:.2f}")
    print(f"El rendimiento es: {rendimiento}")

calcular_promedio_y_rendimiento()
