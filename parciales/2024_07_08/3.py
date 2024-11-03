def independent_set_greedy(grafo):
    iset = {}
    vs = sorted(grafo, key=lambda v: len(grafo.adyacentes(v)))

    for v in vs:
        if all(w not in iset for w in grafo.adyacentes(v)):
            iset.add(v)

    return iset
