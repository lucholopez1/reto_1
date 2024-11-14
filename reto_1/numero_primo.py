def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def filtrar_primos(lista):
    primos = [num for num in lista if es_primo(num)]
    return primos


# Solicitar lista de números al usuario
entrada = input("Ingrese una lista de números separados por comas: ")
numeros = [int(num.strip()) for num in entrada.split(",")]

# Filtrar y mostrar los números primos
primos = filtrar_primos(numeros)
print("Números primos:", primos)