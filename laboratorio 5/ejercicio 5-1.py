edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

edades.sort()
edad_minima = edades[0]
edad_maxima = edades[-1]
edades.append(edad_minima)
edades.append(edad_maxima)

if len(edades) % 2 == 1:
    edad_mediana = edades[len(edades) // 2]
else:
    medio1 = edades[len(edades) // 2 - 1]
    medio2 = edades[len(edades) // 2]
    edad_mediana = (medio1 + medio2) / 2

edad_promedio = sum(edades) / len(edades)

rango_edades = edad_maxima - edad_minima

diferencia_minima = abs(edad_minima - edad_promedio)
diferencia_maxima = abs(edad_maxima - edad_promedio)

print("Edades ordenadas:", edades)
print("Edad mínima:", edad_minima)
print("Edad máxima:", edad_maxima)
print("Edad mediana:", edad_mediana)
print("Edad promedio:", edad_promedio)
print("Rango de edades:", rango_edades)
print("Diferencia mínima:", diferencia_minima)
print("Diferencia máxima:", diferencia_maxima)
