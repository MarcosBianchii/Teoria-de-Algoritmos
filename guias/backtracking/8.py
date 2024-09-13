# (★★★) Implementar un algoritmo de backtracking que, dados dos grafos, determine si existe un Isomorfismo entre ambos.

from collections import Counter


def hay_isomorfismo(g1, g2):
    # Chequear la cantidad de vertices
    if len(g1) != len(g2):
        return False

    def grado(grafo, v):
        return sum(1 for _ in grafo.adyacentes(v))

    V = len(g1)
    grados_g1 = {v: grado(g1, v) for v in g1}
    grados_g2 = {v: grado(g2, v) for v in g2}

    # Chequear la distribucion de grados
    if Counter(grados_g1.values()) != Counter(grados_g2.values()):
        return False

    v1s = g1.obtener_vertices()
    v2s = g2.obtener_vertices()

    def pueden_ser(v1, v2, f, g):
        # Chequear los grados de estos vertices
        if grados_g1[v1] != grados_g2[v2]:
            return False

        def grados_adyacentes(grafo, grados, v):
            return Counter(grados[w] for w in grafo.adyacentes(v))

        # Chequear la distribucion de grados adyacentes
        grados_adyacentes_v1 = grados_adyacentes(g1, grados_g1, v1)
        grados_adyacentes_v2 = grados_adyacentes(g2, grados_g2, v2)
        if grados_adyacentes_v1 != grados_adyacentes_v2:
            return False

        # Chequear que si ya tenemos un isomorfismo de los
        # vertices adyacentes, estos tambien sean adyacentes
        adyacentes_v1 = set(g1.adyacentes(v1))
        adyacentes_v2 = set(g2.adyacentes(v2))

        for w in g1.adyacentes(v1):
            if w in f and f[w] not in adyacentes_v2:
                return False

        for w in g2.adyacentes(v2):
            if w in g and g[w] not in adyacentes_v1:
                return False

        return True

    def hay_isomorfismo_rec(i, f, g):
        if i == V:
            return True

        v1 = v1s[i]
        for v2 in v2s:
            if v2 not in g and pueden_ser(v1, v2, f, g):
                f[v1] = v2
                g[v2] = v1

                if hay_isomorfismo_rec(i + 1, f, g):
                    return True

                del f[v1]
                del g[v2]

        return False

    return hay_isomorfismo_rec(0, {}, {})
