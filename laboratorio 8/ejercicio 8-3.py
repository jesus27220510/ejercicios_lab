import random
import string

def generar_contrasena_segura(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = []
    contrasena.append(random.choice(string.ascii_uppercase))  # Al menos una mayúscula
    contrasena.append(random.choice(string.ascii_lowercase))  # Al menos una minúscula
    contrasena.append(random.choice(string.digits))  # Al menos un número
    contrasena.append(random.choice(string.punctuation))  # Al menos un carácter especial

    for _ in range(longitud - 4):
        contrasena.append(random.choice(caracteres))

    random.shuffle(contrasena)
    return ''.join(contrasena)

longitud_contrasena = 12  # Puedes cambiar la longitud aquí
contrasena_generada = generar_contrasena_segura(longitud_contrasena)
print("Contraseña generada:", contrasena_generada)
