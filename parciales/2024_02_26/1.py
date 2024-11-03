def laberinto(tablero, V):
    n = len(tablero)
    m = len(tablero[0])

    mem = [[0] * (m + 1) for _ in range(n + 1)]
    mem[0][1] = V

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            mem[i][j] = max(mem[i - 1][j], mem[i][j - 1]) - \
                tablero[i - 1][j - 1]

    return mem[n][m], construir_solucion(mem, n, m)


def construir_solucion(mem, n, m):
    sol = []

    while n > 1 and m > 1:
        if mem[n - 1][m] > mem[n][m - 1]:
            sol.append("abajo")
            n -= 1
        else:
            sol.append("derecha")
            m -= 1

    for _ in range(n, 1, -1):
        sol.append("abajo")

    for _ in range(m, 1, -1):
        sol.append("derecha")

    sol.reverse()
    return sol


tablero = [
    [0, 0, 6, 1],
    [2, 5, 0, 9],
]

print(laberinto(tablero, 10))
