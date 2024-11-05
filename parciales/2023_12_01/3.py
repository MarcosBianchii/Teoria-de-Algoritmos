def operaciones_hasta_k(k):
    mem = [0] * (k + 1)

    for i in range(1, k + 1):
        mem[i] = 1 + (mem[i - 1] if k %
                      2 == 1 else min(mem[i - 1], mem[i // 2]))

    return mem[k], construir_solucion(mem, k)


def construir_solucion(f, k):
    sol = []

    while k >= 0:
        if k % 2 == 0 and f[k // 2] < f[k - 1]:
            sol.append("duplicar")
            k //= 2
        else:
            sol.append("sumar 1")
            k -= 1

    sol.reverse()
    return sol
