n = int(input("Ingrese un número para la serie de Fibonacci: "))
fib_series = []

if n > 0:
    a, b = 0, 1
    fib_series.append(a)
    while len(fib_series) < n:
        a, b = b, a + b
        fib_series.append(a)

print("La serie de Fibonacci hasta el", n, "ésimo término es:", fib_series)
