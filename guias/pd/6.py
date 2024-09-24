# (★★) Dado el teclado numérico de un celular, y un número inicial k, encontrar la cantidad de posibles números de longitud n empezando por el botón del número inicial k. Restricción: solamente se puede presionar un botón si está arriba, abajo, a izquierda, o derecha del botón actual. Implementar el algoritmo por programación dinámica. Indicar y justificar la complejidad del algoritmo implementado. Ejemplos:

# Para n=1 empezando por cualquier dígito, solamente hay un número válido (el correspondiente dígito)

# Para N=2, depende de con cuál dígito se comienza:

# Empezando por 0, son válidos 00, 08 (cantidad: 2)

# Empezando por 1, son válidos 11, 12, 14 (cantidad: 3)

# Empezando por 2, son válidos 22, 21, 23, 25 (cantidad: 4)

# Empezando por 3, son válidos 33, 32, 36 (cantidad: 3)

# Empezando por 4, son válidos 44, 41, 45, 47 (cantidad: 4)

# Empezando por 5, son válidos 55, 52, 54, 56, 58 (cantidad: 5)

# Empezando por 6, son válidos 66, 63, 65, 69 (cantidad: 4)

# Empezando por 7, son válidos 77, 74, 78 (cantidad: 3)

# Empezando por 8, son válidos 88, 80, 85, 87, 89 (cantidad: 5)

# Empezando por 9, son válidos 99, 96, 98 (cantidad: 3)

def numeros_posibles(k, n):
    """
    f(k, 1) = 1
    f(k, n) = sum(f(ki, n - 1)) / ki in ady(k)

    La complejidad del algoritmo es O(n)
    """
    adyacentes = [
        [0, 8],
        [1, 2, 4],
        [1, 2, 3, 5],
        [2, 3, 6],
        [1, 4, 5, 7],
        [2, 4, 5, 6, 8],
        [3, 5, 6, 9],
        [4, 7, 8],
        [0, 5, 7, 8, 9],
        [6, 8, 9],
    ]

    # O(1)
    mem = [1] * 10

    # O(n)
    for _ in range(2, n + 1):
        # O(1)
        tmp = [0] * 10
        for tecla in range(10):
            # O(1)
            for ady in adyacentes[tecla]:
                tmp[tecla] += mem[ady]

        mem = tmp

    return mem[k]
