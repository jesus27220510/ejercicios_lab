try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")

    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            raise ValueError("No se puede dividir por cero")
    else:
        print("Operación no válida. Ingrese '+', '-', '*' o '/'.")

    print("Resultado: ", resultado)

except ValueError:
    print("Entrada inválida. Ingrese números válidos.")
except Exception as e:
    print("Error")
