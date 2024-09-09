# (★★) Implementar un algoritmo que reciba un grafo y un número n que, utilizando backtracking, indique si es posible pintar cada vértice con n colores de tal forma que no hayan dos vértices adyacentes con el mismo color.

def colorear(grafo, n):
    colores = {}

    def verificar_coloreo(v):
        for w in grafo.adyacentes(v):
            if w in colores and colores[v] == colores[w]:
                return False

        return True

    def colorear_componente(v):
        for color in range(n):
            colores[v] = color

            if verificar_coloreo(v):
                if len(colores) == len(grafo):
                    return True

                for w in grafo.adyacentes(v):
                    if w not in colores:
                        if colorear_componente(w):
                            return True

        del colores[v]
        return False

    for v in grafo:
        if v not in colores:
            if not colorear_componente(v):
                return False

    return True
