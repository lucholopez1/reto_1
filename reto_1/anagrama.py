def filtrar_anagramas(lista_palabras):
    anagramas = []
    for palabra in lista_palabras:
        for otra_palabra in lista_palabras:
            if palabra != otra_palabra and sorted(palabra) == sorted(otra_palabra):
                anagramas.append(palabra)
                break
    return anagramas


# Solicitar lista de palabras al usuario
entrada = input("Ingrese una lista de palabras separadas por comas: ")
lista_palabras = [palabra.strip() for palabra in entrada.split(",")]

# Llamar a la función y mostrar el resultado
resultado = filtrar_anagramas(lista_palabras)
print("Palabras que tienen los mismos caracteres:", resultado)
