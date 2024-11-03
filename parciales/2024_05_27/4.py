def dominating_set_min(grafo, valores):
    optimo = set(grafo)
    ds = set(grafo)
    vs = grafo.obtener_vertices()
    return bt(grafo, vs, 0, optimo, ds, valores)


def bt(grafo, vs, i, optimo, ds, valores):
    if i == len(grafo):
        return ds.copy() if valor(ds, valores) < valor(optimo, valores) else optimo

    ds.remove(vs[i])
    if validar_dominating_set(grafo, ds, vs[i]):
        optimo = bt(grafo, vs, i + 1, optimo, ds, valores)

    ds.add(vs[i])
    return bt(grafo, vs, i + 1, optimo, ds, valores)


def valor(vs, valores):
    suma = 0
    for v in vs:
        suma += valores[v]

    return suma


def validar_dominating_set(grafo, ds, quitado):
    dominado = False
    for v in grafo.adyacentes(quitado):
        if v in ds:
            dominado = True
            continue

        if all(w not in ds for w in grafo.adyacentes(v)):
            return False

    return dominado
