def mayor_suma_consecutivos(numeros):
    if len(numeros) < 2:
        return "La lista debe tener al menos dos elementos."
    
    suma_maxima = numeros[0] + numeros[1]
    for i in range(1, len(numeros) - 1):
        suma_actual = numeros[i] + numeros[i + 1]
        if suma_actual > suma_maxima:
            suma_maxima = suma_actual
    
    return suma_maxima


# Solicitar lista de números al usuario
entrada = input("Ingrese una lista de números separados por comas: ")
numeros = [int(num.strip()) for num in entrada.split(",")]

# Llamar a la función y mostrar el resultado
resultado = mayor_suma_consecutivos(numeros)
print("La mayor suma entre elementos consecutivos es:", resultado)
