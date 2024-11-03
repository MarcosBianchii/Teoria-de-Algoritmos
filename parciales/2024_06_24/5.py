from math import floor, sqrt


def terminos(n):
    perfectos = [i ** 2 for i in range(1, floor(sqrt(n)) + 1)]
    mem = [0] * (n + 1)

    for i in range(1, n + 1):
        mejor = i

        for p in perfectos:
            if p <= i:
                mejor = min(mejor, mem[i - p])
            else:
                break

        mem[i] = mejor + 1

    return mem


def construir_solucion(f, n):
    perfectos = [i ** 2 for i in range(1, floor(sqrt(n)) + 1)]
    sol = []

    while n > 0:
        for i in range(floor(sqrt(n)) - 1, -1, -1):
            p = perfectos[i]
            if f[n - p] == f[n] - 1:
                sol.append(p)
                n -= p
                break

    sol.reverse()
    return sol
