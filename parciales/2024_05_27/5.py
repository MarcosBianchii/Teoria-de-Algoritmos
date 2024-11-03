def dominating_set(grafo, valores):
    n = len(grafo)
    mem = [0] * (n + 1)
    vs = grafo.obtener_vertices()

    mem[1] = mem[2] = valores[vs[0]]

    for i in range(3, n + 1):
        mem[i] = min(mem[i - 1] + valores[vs[i - 1]],
                     mem[i - 2] + valores[vs[i - 2]])

    return construir_solucion(mem, vs, valores)


def construir_solucion(mem, vs, valores):
    i = len(vs)
    sol = []

    while i > 0:
        if mem[i] == mem[i - 1] + valores[vs[i - 1]]:
            sol.append(vs[i - 1])
            i -= 1
        else:
            sol.append(vs[i - 2])
            i -= 2

    sol.reverse()
    return sol
