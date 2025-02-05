def batalla_naval(filas, columnas, b):
    """
    La complejidad del algoritmo es O(n * m * k * l + klogk)
    """
    # O(n + m + n * m)
    n, m = len(filas), len(columnas)
    tablero = [[0] * m for _ in range(n)]
    filas, columnas = filas.copy(), columnas.copy()

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

    def insertar_barco(l):
        """
        La complejidad es O(n * m * l)
        """
        # O(n * m * l)
        for i in range(n):
            for j in range(m):
                if insertar_barco_horizontal(i, j, l):
                    return True

                if insertar_barco_vertical(i, j, l):
                    return True

        return False

    # O(klogk)
    largos = {}
    for l in sorted(b):
        largos[l] = largos.get(l, 0) + 1

    # O (n * m * k * l)
    demanda_cumplida = 0
    while largos:
        l, veces = largos.popitem()

        for _ in range(veces):
            if insertar_barco(l):
                demanda_cumplida += 2 * l
            else:
                break

    return tablero, demanda_cumplida
