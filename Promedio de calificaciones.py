# Calcula el promedio de calificaciones ingresadas
def promedio_calificaciones():
    calificaciones = []
    while True:
        calificacion = float(input("Ingresa una calificación (-1 para terminar): "))
        if calificacion == -1:
            break
        calificaciones.append(calificacion)

    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"El promedio de las calificaciones es: {promedio:.2f}")
    else:
        print("No se ingresaron calificaciones.")

promedio_calificaciones()
