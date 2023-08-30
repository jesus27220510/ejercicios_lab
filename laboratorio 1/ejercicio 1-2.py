n = int(input("Ingrese un número: "))
primos = []

for numero in range(2, n):
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(numero)

print("Los números primos menores que", n, "son:", primos)
