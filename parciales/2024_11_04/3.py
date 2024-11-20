def osvaldo(p):
    n = len(p)
    mem = [0] * (n + 1)
    comp = p[0]

    for i in range(1, n + 1):
        mem[i] = max(mem[i - 1], p[i - 1] - comp)
        comp = min(comp, p[i - 1])

    return mem[i], encontrar_dias(n, mem, comp, p)


def encontrar_dias(n, f, comp, p):
    compra = p.index(comp)

    for i in range(n - 1, -1, -1):
        if p[i] == f[n] + comp:
            return compra, i
