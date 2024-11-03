

def dominating_set_arbol(grafo):
    d = set()
    while len(grafo) > 0:
        # Cada iteracion es O(v)
        hojas, padres = hojas_y_padres(grafo)

        for h in hojas:
            grafo.borrar_vertice(h)

        for p in padres:
            d.add(p)
            grafo.borrar_vertice(p)

    return d


def hojas_y_padres(grafo):
    hojas, padres = set(), set()

    # O(v)
    for v in grafo:
        grado = grafo.grado(v)
        # Caso particular donde me
        # quedo colgado un vertice
        if grado == 0:
            padres.add(v)

        elif grado == 1 and v not in padres:
            hojas.add(v)
            padres.add(next(iter(grafo.adyacentes(v))))

    return hojas, padres
