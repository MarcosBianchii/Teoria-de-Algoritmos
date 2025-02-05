from pulp import LpProblem, LpMaximize, LpVariable, lpSum, value, PULP_CBC_CMD
from collections import Counter


def batalla_naval(filas, columnas, b):
    n, m = len(filas), len(columnas)
    largos = Counter(b)  # O(k)

    def en_rango(casillero):
        i, j = casillero
        return 0 <= i and 0 <= j and i < n and j < m

    def adyacentes_hor(i, j, l):
        for k in range(-1, l + 1):
            yield i - 1, j + k
            yield i + 1, j + k

        yield i, j - 1
        yield i, j + l

    def adyacentes_ver(i, j, l):
        for k in range(-1, l + 1):
            yield i + k, j - 1
            yield i + k, j + 1

        yield i - 1, j
        yield i + l, j

    def entra_horizontal(i, j, l):
        """
        La complejidad es O(l)
        """
        if l > filas[i]:
            return False

        if j + l > m:
            return False

        # O(l)
        if any(columnas[j + k] == 0 for k in range(l)):
            return False

        return True

    def entra_vertical(i, j, l):
        """
        La complejidad es O(l)
        """
        if l > columnas[j]:
            return False

        if i + l > n:
            return False

        # O(l)
        if any(filas[i + k] == 0 for k in range(l)):
            return False

        return True

    prob = LpProblem("Batalla_Naval", LpMaximize)

    # O(n * m)
    ys = [[LpVariable(f"{i}_{j}", cat="Binary")
           for j in range(m)] for i in range(n)]

    # O(n * m * l)
    bs = {l: [] for l in largos}

    for i in range(n):
        for j in range(m):
            for l in largos:
                if entra_vertical(i, j, l):
                    v = LpVariable(f"V_{i}_{j}_{l}", cat="Binary")
                    ady = list(filter(en_rango, adyacentes_ver(i, j, l)))
                    sum_ocu = lpSum(ys[i + k][j] for k in range(l))
                    sum_ady = lpSum(1 - ys[Ai][Aj] for Ai, Aj in ady)
                    prob += v * (l + len(ady)) <= sum_ocu + sum_ady
                    bs[l].append(v)

                # No repetir los de largo 1.
                if l > 1 and entra_horizontal(i, j, l):
                    h = LpVariable(f"H_{i}_{j}_{l}", cat="Binary")
                    ady = list(filter(en_rango, adyacentes_hor(i, j, l)))
                    sum_ocu = lpSum(ys[i][j + k] for k in range(l))
                    sum_ady = lpSum(1 - ys[Ai][Aj] for Ai, Aj in ady)
                    prob += h * (l + len(ady)) <= sum_ocu + sum_ady
                    bs[l].append(h)

    # O(l)
    for l, barcos in bs.items():
        prob += lpSum(barcos) <= largos[l]

    # O(n)
    for i in range(n):
        prob += lpSum(ys[i]) <= filas[i]

    # O(m)
    for j in range(m):
        prob += lpSum(ys[i][j] for i in range(n)) <= columnas[j]

    prob += 2 * lpSum(l * lpSum(bs[l]) for l in largos)
    prob.solve(PULP_CBC_CMD(msg=False))

    # O(n * m)
    tablero = [[0] * m for _ in range(n)]

    cumplido = 0  # O(n * m * l)
    for l in filter(lambda l: largos[l] > 0, bs):
        for barco in filter(lambda b: bool(value(b)), bs[l]):
            largos[l] -= 1

            orientacion, i, j, l = barco.name.split("_")
            i, j, l = int(i), int(j), int(l)
            if orientacion == "V":
                for i in range(i, i + l):
                    tablero[i][j] = 1

            elif orientacion == "H":
                for j in range(j, j + l):
                    tablero[i][j] = 1

            cumplido += 2 * l

    return tablero, cumplido
