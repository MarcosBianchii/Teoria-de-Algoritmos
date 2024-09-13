# (★★★) Un set dominante(Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice de G: o bien(i) pertenece a D o bien(ii) es adyacente a un vértice en D. Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho grafo con la mínima cantidad de vértices.

def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()

    def es_dominating_set(conjunto):
        vs = set(conjunto)

        for v in conjunto:
            for w in grafo.adyacentes(v):
                vs.add(w)

        return len(vs) == len(grafo)

    def calcular_min_set(i, min_set):
        if es_dominating_set(min_set):
            return min_set.copy()

        if i == len(grafo):
            return []

        v = vertices[i]
        min_set.append(v)
        con = calcular_min_set(i + 1, min_set)

        min_set.pop()
        sin = calcular_min_set(i + 1, min_set)

        return min(con, sin, key=len)

    return calcular_min_set(0, [])
