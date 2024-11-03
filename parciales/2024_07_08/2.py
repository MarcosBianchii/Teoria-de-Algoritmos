from ..grafo import Grafo
from math import sqrt
from utils import encontrar_camino


def dist(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def ford_fulkerson(grafo, s, t):
    flujos = {(v, w): 0 for v in grafo for w in grafo.adyacentes(v)}
    residual = grafo.copy()

    while (camino := encontrar_camino(residual, s, t)) is not None:
        for i in range(1, len(camino)):
            v = camino[i - 1]
            w = camino[i]

            flujos[(v, w)] += 1
            residual.borrar_arista(v, w)

    return flujos


def cruz_roja(ambulancias, pedidos, k):
    grafo = Grafo(dirigdo=True)
    grafo.agregar_vertice("fuente")
    grafo.agregar_vertice("sumidero")

    for a in ambulancias:
        grafo.agregar_vertice(a)
        grafo.agregar_arista("fuente", a, 1)

        for p in pedidos:
            if p not in grafo:
                grafo.agregar_vertice(p)
                grafo.agregar_arista(p, "fuente", 1)
            if dist(a, p) <= k:
                grafo.agregar_arista(a, p, 1)

    flujos = ford_fulkerson(grafo, "fuente", "sumidero")
