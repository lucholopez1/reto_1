def calculadora(a, b, operador):
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        if b != 0:
            return a / b
        else:
            return "Error: División por cero"
    else:
        return "Operador no válido"


# Solicitar datos al usuario
while True:
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        operador = input("Ingrese el operador (+, -, *, /): ")

        # Llamar a la función y mostrar el resultado
        resultado = calculadora(a, b, operador)
        print("Resultado:", resultado)

        # Preguntar si quiere realizar otra operación
        continuar = input("¿Desea realizar otra operación? (s/n): ")
        if continuar.lower() != "s":
            break
    except ValueError:
        print("Por favor, ingrese un número válido.")
