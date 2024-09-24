# (★) Implementar un algoritmo que, utilizando programación dinámica, obtenga el valor del n-ésimo número de fibonacci. Indicar y justificar la complejidad del algoritmo implementado. Definición:

# n = 0 --> Debe devolver 1
# n = 1 --> Debe devolver 1
# n --> Debe devolver la suma entre los dos anteriores números de fibonacci (los fibonacci n-2 y n-1)

def fibonacci(n):
    """
    f(0) = 1
    f(1) = 1
    f(n) = f(n - 1) + f(n - 2)

    La complejidad del algoritmo es O(n)
    """
    a = 1
    b = 1

    # O(n)
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b
