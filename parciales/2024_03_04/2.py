def pepe(monedas):
    n, m = len(monedas), monedas
    mem = [[0] * n for _ in range(n + 1)]

    for i in range(n):
        mem[1][i] = m[i]

    for i in range(n - 1):
        mem[2][i] = max(m[i], m[i + 1])

    for i in range(3, n + 1):
        for j in range(n - i + 1):
            pm = m[j] + mem[i - 2][j + 1 + (m[j + 1] < m[j + i - 1])]
            um = m[j + i - 1] + mem[i - 2][j + (m[j] < m[j + i - 2])]
            mem[i][j] = max(pm, um)

    return mem[n][0]
