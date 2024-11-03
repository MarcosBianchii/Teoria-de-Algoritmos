# (★★) Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a ∣V∣, devuelva si es posible obtener un subconjunto de n vertices tal que ningun par de vertices sea adyacente entre si.

def no_adyacentes(grafo, n):
    def hay_adyacentes(elegidos, agregado):
        for v in grafo.adyacentes(agregado):
            if v in elegidos:
                return True

        return False

    vs = grafo.obtener_vertices()

    def bt(i, optimo, elegidos):
        if len(elegidos) == n:
            return elegidos.copy()

        if i == len(grafo):
            return elegidos.copy() if len(elegidos) > len(optimo) else optimo

        if n > len(elegidos) + len(grafo) - i:
            return optimo

        elegidos.add(vs[i])
        if not hay_adyacentes(elegidos, vs[i]):
            optimo = bt(i + 1, optimo, elegidos)
            if len(optimo) == n:
                return optimo

        elegidos.remove(vs[i])
        return bt(i + 1, optimo, elegidos)

    if len(max_is := bt(0, set(), set())) >= n:
        return list(max_is)
