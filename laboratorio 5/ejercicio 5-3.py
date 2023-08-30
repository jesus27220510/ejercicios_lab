lista1 = list(range(1, 11))
lista2 = list(range(5, 16))
lista3 = list(range(10, 21))

conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = set(lista3)

conjunto_comun = conjunto1 & conjunto2 & conjunto3

conjunto_union = conjunto1 | conjunto2 | conjunto3

conjunto_diferencia = conjunto1 - conjunto3

tupla1 = tuple(conjunto1)
tupla2 = tuple(conjunto2)
tupla3 = tuple(conjunto3)

suma_tuplas = (tupla1[0] + tupla1[-1],
               tupla2[0] + tupla2[-1],
               tupla3[0] + tupla3[-1])

print("Conjunto de números en las tres listas:", conjunto_comun)
print("Conjunto de números en al menos una lista:", conjunto_union)
print("Conjunto de números en la primera lista pero no en la última:", conjunto_diferencia)
print("Suma de primeros y últimos elementos de las tuplas:", suma_tuplas)
