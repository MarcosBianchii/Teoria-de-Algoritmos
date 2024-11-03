# (★★★) Un set dominante(Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice de G: o bien(i) pertenece a D o bien(ii) es adyacente a un vértice en D. Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho grafo con la mínima cantidad de vértices.

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

    return list(bt(0, set(vs), set(vs)))
