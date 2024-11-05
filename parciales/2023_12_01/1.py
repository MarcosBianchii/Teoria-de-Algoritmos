def vertex_cover_min(grafo):
    vs = grafo.obtener_vertices()

    def validar_vertex_cover(vcover, quitado):
        for w in grafo.adyacentes(quitado):
            if w not in vcover:
                return False

        return True

    def bt(i, optimo, vcover):
        if i == len(grafo):
            return vcover.copy() if len(vcover) < len(optimo) else optimo

        vcover.remove(vs[i])
        if validar_vertex_cover(vcover, vs[i]):
            optimo = bt(i + 1, optimo, vcover)

        vcover.add(vs[i])
        return bt(i + 1, optimo, vcover)

    return bt(0, set(vs), set(vs))
