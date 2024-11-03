def dominating_set(grafo):
    vs = grafo.obtener_vertices()

    def validar_dominating_set(ds, quitado):
        dominado = False
        for w in grafo.adyacentes(quitado):
            if w in ds:
                dominado = True
                continue

            if all(u not in ds for u in grafo.adyacentes(w)):
                return False

        return dominado

    def bt(i, optimo, ds):
        if i == len(grafo):
            return ds.copy() if len(ds) < len(optimo) else optimo

        ds.remove(vs[i])
        if validar_dominating_set(ds, vs[i]):
            optimo = bt(i + 1, optimo, ds)

        ds.add(vs[i])
        return bt(i + 1, optimo, ds)

    return bt(0, set(vs), set(vs))
