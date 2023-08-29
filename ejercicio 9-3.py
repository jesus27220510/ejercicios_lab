import random
import string

def generar_contrasena(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_especiales):
    caracteres = ''
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiales:
        caracteres += string.punctuation

    if caracteres:
        return ''.join(random.choice(caracteres) for _ in range(longitud))
    else:
        raise ValueError("Debes incluir al menos un tipo de caracter")

try:
    longitud = int(input("Longitud de la contraseña: "))
    mayusculas = input("Incluir mayúsculas (S/N): ").upper() == 'S'
    minusculas = input("Incluir minúsculas (S/N): ").upper() == 'S'
    numeros = input("Incluir números (S/N): ").upper() == 'S'
    especiales = input("Incluir caracteres especiales (S/N): ").upper() == 'S'

    contrasena = generar_contrasena(longitud, mayusculas, minusculas, numeros, especiales)
    print(f"Contraseña generada: {contrasena}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
