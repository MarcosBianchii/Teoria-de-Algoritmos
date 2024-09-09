# (★★) Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover. Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo Vertex Cover del mismo (es decir, que sea el conjunto de tamaño mínimo).

def vertex_cover_min(grafo):
    def grado(v):
        return sum(1 for _ in grafo.adyacentes(v))

    vertices = grafo.obtener_vertices()
    E = sum(grado(v) for v in grafo) / 2

    def es_vertex_cover(vs):
        visitados = set()

        aristas = 0
        for v in vs:
            visitados.add(v)
            for w in grafo.adyacentes(v):
                aristas += 1 if w not in visitados else 0

        return aristas == E

    def min_vc(i, subset):
        if es_vertex_cover(subset):
            return subset.copy()

        if i == len(grafo):
            return None

        subset.append(vertices[i])
        con = min_vc(i + 1, subset)

        subset.pop()
        sin = min_vc(i + 1, subset)

        if not con or not sin:
            return con if con else sin

        return min(con, sin, key=len)

    return min_vc(0, [])
