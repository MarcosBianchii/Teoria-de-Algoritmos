# (★) Dada una red residual, dar un algoritmo que encuentre un camino de aumento que minimice el número de aristas utilizadas.

from collections import deque


def construir_camino(padres, t):
    camino = [t]

    # O(v)
    while (padre := padres.get(camino[-1])) is not None:
        camino.append(padre)

    # O(v)
    camino.reverse()
    return camino


def encontrar_camino(red, s, t):
    q = deque([s])
    padres = {}

    # O(v + a)
    while q:
        v = q.popleft()
        if v == t:
            return construir_camino(padres, t)

        for w in red.adyacentes(v):
            if w not in padres:
                padres[w] = v
                q.append(w)
