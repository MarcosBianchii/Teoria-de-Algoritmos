# (★) Dada una red residual, dar un algoritmo que encuentre un camino de aumento que minimice el número de aristas utilizadas.

from collections import deque
from ..grafo import Grafo


def construir_camino(padres, fin):
    camino = [fin]

    # O(v)
    while (padre := padres[camino[-1]]) is not None:
        camino.append(padre)

    # O(v)
    camino.reverse()
    return camino


def encontrar_camino(red: Grafo, s, t):
    padres = {s: None}
    q = deque([s])

    # O(v + a)
    while q:
        v = q.popleft()
        if v == t:
            return construir_camino(padres, t)

        for w in red.adyacentes(v):
            if w not in padres:
                padres[w] = v
                q.append(w)
