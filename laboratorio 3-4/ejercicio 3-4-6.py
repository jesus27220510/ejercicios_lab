num1 = 8
num2 = 6

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
modulo = num1 % num2
division_entera = num1 // num2
potencia = num1 ** num2

formato = "{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {:.2f}\n{} % {} = {}\n{} // {} = {}\n{} ** {} = {}"

resultado_formateado = formato.format(num1, num2, suma,
                                      num1, num2, resta,
                                      num1, num2, multiplicacion,
                                      num1, num2, division,
                                      num1, num2, modulo,
                                      num1, num2, division_entera,
                                      num1, num2, potencia)

print(resultado_formateado)
