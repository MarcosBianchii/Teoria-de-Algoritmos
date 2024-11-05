def k_ciclo(grafo, k):
    def dfs(camino, visitados):
        if len(camino) > k:
            return False

        v = camino[-1]
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                camino.append(w)

                if dfs(camino, visitados):
                    return True

                visitados.remove(w)
                camino.pop()

            elif len(camino) == k - 1 and w == camino[0]:
                camino.append(w)
                return True

        return False

    for v in grafo:
        camino = [v]
        if dfs(camino, set(camino)):
            return camino

    return []
