# (★★) Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un máximo Independent Set del mismo.

def independent_set(grafo):
    def hay_adyacentes(vs):
        if not vs:
            return False

        ultimo = vs[-1]
        for i in range(len(vs) - 1):
            v = vs[i]
            if grafo.estan_unidos(ultimo, v):
                return True

        return False

    vertices = grafo.obtener_vertices()

    def independent_set(i, indeps):
        if hay_adyacentes(indeps):
            return []

        if i == len(grafo):
            return indeps.copy()

        indeps.append(vertices[i])
        con = independent_set(i + 1, indeps)

        indeps.pop()
        sin = independent_set(i + 1, indeps)

        return max(con, sin, key=len)

    return independent_set(0, [])
