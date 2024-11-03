# (★★) Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover. Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo Vertex Cover del mismo (es decir, que sea el conjunto de tamaño mínimo).

def vertex_cover_min(grafo):
    vs = grafo.obtener_vertices()

    def validar_vertex_cover(vc, quitado):
        for v in grafo.adyacentes(quitado):
            if v not in vc:
                return False

        return True

    def bt(i, optimo, vc):
        if i == len(grafo):
            return vc.copy() if len(vc) < len(optimo) else optimo

        vc.remove(vs[i])
        if validar_vertex_cover(vc, vc[i]):
            optimo = bt(i + 1, optimo, vc)

        vc.add(vs[i])
        return bt(i + 1, optimo, vc)

    return list(bt(0, set(vs), set(vs)))
