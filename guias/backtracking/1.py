# (★★) Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a ∣V∣, devuelva si es posible obtener un subconjunto de n vertices tal que ningun par de vertices sea adyacente entre si.

def no_adyacentes(grafo, n):
    def hay_adyacentes(elegidos):
        if not elegidos:
            return False

        ultimo = elegidos[-1]
        for i in range(len(elegidos) - 1):
            w = elegidos[i]
            if grafo.estan_unidos(ultimo, w):
                return True

        return False

    vertices = grafo.obtener_vertices()

    def no_adyacentes_rec(i, elegidos):
        # Tengo algun adyacente
        if hay_adyacentes(elegidos):
            return False

        # Consegui los n no adyacentes
        if len(elegidos) == n:
            return True

        # Me quede sin nuevos vertices
        if i == len(grafo):
            return False

        # Ya no llego
        if n > len(elegidos) + len(grafo) - i:
            return False

        v = vertices[i]
        elegidos.append(v)
        if no_adyacentes_rec(i + 1, elegidos):
            return True

        elegidos.pop()
        if no_adyacentes_rec(i + 1, elegidos):
            return True

        return False

    elegidos = []
    if no_adyacentes_rec(0, elegidos):
        return elegidos

    return None
