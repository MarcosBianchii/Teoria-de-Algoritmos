# (★★) Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un máximo Independent Set del mismo.

def independent_set(grafo):
    vs = grafo.obtener_vertices()

    def validar_independent_set(iset, agregado):
        for v in grafo.adyacentes(agregado):
            if v in iset:
                return False

        return True

    def bt(i, optimo, iset):
        if i == len(grafo):
            return iset.copy() if len(iset) > len(optimo) else optimo

        iset.add(vs[i])
        if validar_independent_set(iset, vs[i]):
            optimo = bt(i + 1, optimo, iset)

        iset.remove(vs[i])
        return bt(i + 1, optimo, iset)

    return list(bt(0, set(), set()))
