from ..grafo import Grafo


def incidencias(grafo):
    incs = {v: [] for v in grafo}

    for v in grafo:
        for w in grafo.adyacentes(v):
            incs[w].append(v)

    return incs


def camino_mas_largo(grafo):
    mem = {v: 0 for v in grafo}
    incs = incidencias(grafo)
    vs = sorted(grafo)

    for v in vs:
        mem[v] = 1 + (max(mem[w] for w in incs[v])) if len(incs[v]) > 0 else 0

    return mem


def construir_solucion(f, grafo):
    incs = incidencias(grafo)
    v = max(f.keys(), key=lambda x: f[x])
    sol = [v]

    while len(incs[v]) > 0:
        for u in incs[v]:
            if f[u] == f[v] - 1:
                sol.append(u)
                v = u
                break

    sol.reverse()
    return sol


grafo = Grafo(dirigido=True, vertices_init=range(1, 6))
grafo.agregar_arista(1, 2)
grafo.agregar_arista(1, 4)
grafo.agregar_arista(2, 4)
grafo.agregar_arista(2, 5)
grafo.agregar_arista(3, 4)
grafo.agregar_arista(4, 5)


mem = camino_mas_largo(grafo)
print(construir_solucion(mem, grafo))
