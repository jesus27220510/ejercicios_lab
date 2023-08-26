mensaje = input("Ingrese el mensaje a cifrar: ")
desplazamiento = int(input("Ingrese el desplazamiento: "))
mensaje_cifrado = ""

for char in mensaje:
    if char.isalpha():
        offset = ord('A') if char.isupper() else ord('a')
        cifrado = (ord(char) - offset + desplazamiento) % 26 + offset
        mensaje_cifrado += chr(cifrado)
    else:
        mensaje_cifrado += char

print("Mensaje cifrado:", mensaje_cifrado)
