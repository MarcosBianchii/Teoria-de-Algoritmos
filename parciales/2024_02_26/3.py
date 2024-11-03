def k_core(grafo, k):
    grafo = grafo.copy()

    while len(grafo) > 0:
        v = min(grafo, key=grafo.grado)
        if grafo.grado(v) >= k:
            return grafo

        for w in grafo.adyacentes(v):
            grafo.borrar_arista(v, w)

        grafo.borrar_vertice(v)

    return grafo
