from ..grafo import Grafo


def max_clique(grafo: Grafo):
    vs = grafo.obtener_vertices()

    def validar_clique(clique):
        ultimo = clique[-1]

        for i in range(len(clique) - 1):
            if not grafo.estan_unidos(vs[i], ultimo):
                return False

        return True

    def bt(i, clique):
        if not validar_clique(clique):
            return []

        if i == len(vs):
            return clique

        con = bt(i + 1, clique + [vs[i]])
        sin = bt(i + 1, clique)
        return max(con, sin, key=len)

    return bt(0, [])
