from copy import deepcopy
from codigo.aprox import batalla_naval as batalla_naval_aprox


def batalla_naval(filas, columnas, b):
    """
    La complejidad del algoritmo es O(2^k * n * m * l)
    """
    # O(n + m + klogk)
    n, m = len(filas), len(columnas)
    total = sum(filas) + sum(columnas)
    filas, columnas = filas.copy(), columnas.copy()
    b = sorted(b, reverse=True)

    def en_rango(i, j):
        return 0 <= i and 0 <= j and i < n and j < m

    def insertar_barco_horizontal(i, j, tablero, l):
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

    def insertar_barco_vertical(i, j, tablero, l):
        """
        La complejidad es O(l)
        """
        if i + l > n:
            return False

        if l > columnas[j]:
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

    def quitar_barco_horizontal(i, j, tablero, l):
        """
        La complejidad es O(l)
        """
        # O(l)
        filas[i] += l
        for p in range(l):
            tablero[i][j + p] = 0
            columnas[j + p] += 1

    def quitar_barco_vertical(i, j, tablero, l):
        """
        La complejidad es O(l)
        """
        # O(l)
        columnas[j] += l
        for p in range(l):
            tablero[i + p][j] = 0
            filas[i + p] += 1

    def bt(r, opt, opt_acc, parcial, acc):
        """
        La complejidad es O(2^k * n * m * l)
        """
        if r == len(b):
            # O(n * m)
            return (deepcopy(parcial), acc) if acc > opt_acc else (opt, opt_acc)

        # O(k)
        if acc + 2 * sum(b[r:]) <= opt_acc:
            return opt, opt_acc

        # O(n * m * l)
        l = b[r]
        for i in range(n):
            for j in range(m):
                if insertar_barco_horizontal(i, j, parcial, l):
                    opt, opt_acc = bt(r + 1, opt, opt_acc, parcial, acc + 2 * l)
                    if opt_acc == total:
                        return opt, opt_acc

                    quitar_barco_horizontal(i, j, parcial, l)

                if insertar_barco_vertical(i, j, parcial, l):
                    opt, opt_acc = bt(r + 1, opt, opt_acc, parcial, acc + 2 * l)
                    if opt_acc == total:
                        return opt, opt_acc

                    quitar_barco_vertical(i, j, parcial, l)

        return bt(r + 1, opt, opt_acc, parcial, acc)

    # O(2^k * n * m * l)
    vacio = [[0] * m for _ in range(n)]
    aprox, cumplido = batalla_naval_aprox(filas, columnas, b)
    return bt(0, aprox, cumplido, vacio, 0)
