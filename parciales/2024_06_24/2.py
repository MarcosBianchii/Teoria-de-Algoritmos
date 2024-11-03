def viajante_greedy(grafo, v):
    camino = [v]
    visitados = set([v])

    while len(visitados) < len(grafo):
        for w in grafo.adyacentes(camino[-1]):
            if w not in visitados:
                proximo = min(proximo)

        proximo = min((w for w in grafo.adyacentes(camino[-1]) if w not in visitados),
                      key=lambda w: grafo.peso_arista(camino[-1], w))

        camino.append(proximo)
        visitados.add(proximo)

    camino.append(v)
    return camino
