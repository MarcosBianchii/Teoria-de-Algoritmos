from collections import Counter


def conseguir_barcos(tablero):
    """
    La complejidad del algoritmo es O(n * m)
    """
    # O(n * m)
    tablero = tablero.copy()
    n, m = len(tablero), len(tablero[0])

    def en_rango(casillero):
        i, j = casillero
        return 0 <= i and 0 <= j and i < n and j < m

    def siguientes(i, j):
        yield i, j + 1
        yield i + 1, j

    def tomar_barco(i, j):
        if tablero[i][j] == 0:
            return 0

        largo = 0
        tablero[i][j] = 0
        for i, j in filter(en_rango, siguientes(i, j)):
            largo += tomar_barco(i, j)

        return largo + 1

    # O(n * m)
    barcos = []
    for i in range(n):
        for j in range(m):
            if tablero[i][j] == 1:
                largo = tomar_barco(i, j)
                barcos.append(largo)

    return barcos


def validador_batalla_naval(filas, columnas, b, solucion):
    """
    La complejidad del validador es O(n * m + k)
    """
    n, m = len(filas), len(columnas)

    # Validar que el tablero solución tiene la misma
    # cantidad de filas que el original.
    if len(solucion) != n:
        return False

    # O(n)
    #
    # Validar que el tablero solución tiene la misma
    # cantidad de columnas que el original en cada fila.
    for i in range(n):
        if m != len(solucion[i]):
            return False

    # O(n * m)
    #
    # Validar que se cumplen las restricciones por fila.
    for i in range(n):
        if sum(solucion[i]) != filas[i]:
            return False

    # O(n * m)
    #
    # Validar que se cumplen las restricciones por columna.
    for j in range(m):
        if sum(solucion[i][j] for i in range(n)) != columnas[j]:
            return False

    def en_rango(i, j):
        return 0 <= i and 0 <= j and i < n and j < m

    def giros(i, j):
        yield (i, j - 1), (i - 1, j)
        yield (i - 1, j), (i, j + 1)
        yield (i, j + 1), (i + 1, j)
        yield (i + 1, j), (i, j - 1)

    def hay_giro(i, j):
        for (Pi, Pj), (Qi, Qj) in giros(i, j):
            if not en_rango(Pi, Pj) or not en_rango(Qi, Qj):
                continue

            if solucion[Pi][Pj] + solucion[Qi][Qj] == 2:
                return True

        return False

    def hay_diagonal(i, j):
        for Di in [i - 1, i + 1]:
            for Dj in [j - 1, j + 1]:
                if en_rango(Di, Dj) and solucion[Di][Dj] == 1:
                    return True

        return False

    # O(n * m)
    #
    # Validar que no haya adyacencias.
    for i in range(n):
        for j in range(m):
            if solucion[i][j] == 1:
                if hay_giro(i, j) or hay_diagonal(i, j):
                    return False

    # O(n * m)
    barcos = conseguir_barcos(solucion)

    # Validar que no hay más barcos en la solución
    # que en el arreglo de barcos.
    if len(b) < len(barcos):
        return False

    # O(k)
    #
    # Validar que hay a lo sumo las mísma cantidad
    # de barcos para cada largo como en el arreglo
    # de barcos.
    largos = Counter(b)
    for l, q in Counter(barcos).items():
        if l not in largos:
            return False

        if largos[l] < q:
            return False

    return True
