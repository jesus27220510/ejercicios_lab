frase = input("Ingrese una frase: ")
texto_limpio = "".join(filter(str.isalnum, frase)).lower()

if texto_limpio == texto_limpio[::-1]:
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")
