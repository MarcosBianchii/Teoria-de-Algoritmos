def vertex_cover_greedy(grafo):
    vcover = set()

    for v in grafo:
        for w in grafo.adyacentes(v):
            if v not in vcover and w not in vcover:
                vcover.add(max(v, w, key=grafo.grado))

    return vcover
