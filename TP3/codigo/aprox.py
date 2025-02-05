from heapq import heappush, heappop, heapify
from collections import Counter


def batalla_naval(filas, columnas, b):
    """
    La complejidad del algoritmo es O(n * m + (n + m) * (log(n + m) + k * (max(n, m) * l - l^2)) + klogk)
    """
    # O(n * m)
    n, m = len(filas), len(columnas)
    tablero = [[0] * m for _ in range(n)]
    filas = filas.copy()
    columnas = columnas.copy()

    def en_rango(i, j):
        return 0 <= i and 0 <= j and i < n and j < m

    def insertar_barco_horizontal(i, j, l):
        """
        La complejidad es O(l)
        """
        if j + l > m:
            return False

        if l > filas[i]:
            return False

        # O(l)
        if any(columnas[j + k] == 0 for k in range(l)):
            return False

        # O(l)
        for Ci in range(i - 1, i + 2):
            for Cj in range(j - 1, j + l + 1):
                if en_rango(Ci, Cj) and tablero[Ci][Cj] == 1:
                    return False

        # O(l)
        filas[i] -= l
        for k in range(l):
            tablero[i][j + k] = 1
            columnas[j + k] -= 1

        return True

    def insertar_barco_vertical(i, j, l):
        """
        La complejidad es O(l)
        """
        if i + l > n:
            return False

        if l > columnas[j]:
            return False

        # O(l)
        if any(tablero[i + k][j] == 1 for k in range(l)):
            return False

        # O(l)
        if any(filas[i + k] == 0 for k in range(l)):
            return False

        # O(l)
        for Ci in range(i - 1, i + l + 1):
            for Cj in range(j - 1, j + 2):
                if en_rango(Ci, Cj) and tablero[Ci][Cj] == 1:
                    return False

        # O(l)
        columnas[j] -= l
        for k in range(l):
            tablero[i + k][j] = 1
            filas[i + k] -= 1

        return True

    def intentar_por_fila(l, i):
        """
        La complejidad es O(m * l - l^2)
        """
        # O(m * l - l^2)
        for j in range(m - l + 1):
            if insertar_barco_horizontal(i, j, l):
                return True

        return False

    def intentar_por_columna(l, j):
        """
        La complejidad es O(n * l - l^2)
        """
        # O(n * l - l^2)
        for i in range(n - l + 1):
            if insertar_barco_vertical(i, j, l):
                return True

        return False

    # O(n + m)
    fil = [(-f, 0, i, intentar_por_fila) for i, f in enumerate(filas)]
    col = [(-c, 1, j, intentar_por_columna) for j, c in enumerate(columnas)]
    restricciones = fil + col
    heapify(restricciones)

    # O(klogk)
    largos = Counter(b)
    b = sorted(largos, reverse=True)

    # O((n + m) * (log(n + m) + k * (max(n, m) * l - l^2)))
    cumplido = 0
    while restricciones:
        res = heappop(restricciones)
        v, t, ij, f = -res[0], res[1], res[2], res[3]

        for l in filter(lambda l: l in largos, b):
            if f(l, ij):
                cumplido += 2 * l
                if v - l > 0:
                    heappush(restricciones, (l - v, t, ij, f))
                if largos[l] == 1:
                    del largos[l]
                else:
                    largos[l] -= 1
                break

    return tablero, cumplido
