def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertir a minúsculas para evitar diferencias de mayúsculas/minúsculas
    longitud = len(palabra)

    for i in range(longitud // 2):  # Iterar hasta la mitad de la palabra
        if palabra[i] != palabra[longitud - i - 1]:  # Comparar extremos opuestos
            return False

    return True  # Si se completó el bucle sin diferencias, es palíndromo


# Ejemplo de uso
palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
