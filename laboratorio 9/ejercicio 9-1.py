try:
    temperatura = float(input("Ingrese la temperatura: "))
    unidad = input("Ingrese la unidad (C o F): ").upper()

    if unidad == 'C':
        resultado = temperatura * 9/5 + 32
        print(f"{temperatura}°C equivale a {resultado:.2f}°F")
    elif unidad == 'F':
        resultado = (temperatura - 32) * 5/9
        print(f"{temperatura}°F equivale a {resultado:.2f}°C")
    else:
        print("Unidad no válida. Ingrese 'C' o 'F'.")

except ValueError:
    print("Entrada inválida. Ingrese un número válido.")
