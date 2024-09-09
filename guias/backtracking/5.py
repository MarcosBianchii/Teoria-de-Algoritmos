# (★★) Un camino hamiltoniano, es un camino de un grafo, que visita todos los vértices del grafo una sola vez. Implementar un algoritmo por backtracking que encuentre un camino hamiltoniano de un grafo dado.

def camino_hamiltoniano(grafo):
    def existe_hamilton(v, camino, visitados):
        if len(camino) == len(grafo):
            return True

        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                camino.append(w)

                if existe_hamilton(w, camino, visitados):
                    return True

                visitados.remove(w)
                camino.pop()

        return False

    for v in grafo:
        camino = [v]
        if existe_hamilton(v, camino, set(camino)):
            return camino

    return []
