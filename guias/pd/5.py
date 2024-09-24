# (★) Dado un laberinto representado por una grilla, queremos calcular la ganancia máxima que existe desde la posición (0,0) hasta la posición NxM. Los movimientos permitidos son, desde la esquina superior izquierda (el (0,0)), nos podemos mover hacia abajo o hacia la derecha. Pasar por un casillero determinado (i,j) nos da una ganancia de V_{ij}. Implementar un algoritmo que, por programación dinámica, obtenga la máxima ganancia a través del laberinto. Hacer una reconstrucción del camino que se debe transitar. Indicar y justificar la complejidad del algoritmo implementado. Si hay algunos lugares por los que no podemos pasar (obstáculos), ¿cómo se debe modificar para resolver el mismo problema?

def laberinto(matriz):
    """
    f(n, m) = v[n][m] + max(f(n - 1, m), f(n, m - 1))

    Si tuvieramos que considerar obstaculos, debemos setear un valor de 0 en la matriz
    y la ecuacion de recurrencia seria la siguiente:

    f(n, m) = 0 if es_obstaculo(n, m) else v[n][m] + max(f(n - 1, m), f(n, m - 1))

    Tambien habria que tener en cuenta como inicializamos la matriz de memoria.

    La complejidad del algoritmo es O(n * m)
    """
    if not matriz:
        return 0

    def laberinto_pd(n, m, v):
        # O(n * m)
        mem = [[0] * (m + 1) for _ in range(n + 1)]

        # O(n)
        for i in range(1, n + 1):
            # O(m)
            for j in range(1, m + 1):
                mem[i][j] = v[i - 1][j - 1] + max(mem[i - 1][j], mem[i][j - 1])

        return mem

    def construir_solucion(n, m, f):
        sol = []

        # O(min(n, m))
        while n > 1 and m > 1:
            if f[n - 1][m] > f[n][m - 1]:
                sol.append("abajo")
                n -= 1
            else:
                sol.append("derecha")
                m -= 1

        # O(n)
        while n > 1:
            sol.append("abajo")
            n -= 1

        # O(m)
        while m > 1:
            sol.append("derecha")
            m -= 1

        # O(n + m)
        sol.reverse()
        return sol

    n = len(matriz)
    m = len(matriz[0])
    f = laberinto_pd(n, m, matriz)
    return construir_solucion(n, m, f)
