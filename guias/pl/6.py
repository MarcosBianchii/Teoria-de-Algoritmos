# (★★★) Implementar un modelo de programación lineal que nos obtenga el Árbol de Tendido mínimo de un grafo.


from pulp import LpProblem, LpMinimize, LpVariable, lpSum, value
from itertools import chain, combinations


def subconjuntos_de_vertices(grafo):
    return chain.from_iterable(set(combinations(grafo, n)) for n in range(1, len(grafo)))


def tendido_minimo(grafo):
    es_dirigido = False

    aristas = {}
    for v in grafo:
        for w in grafo.adyacentes(v):
            aristas[(v, w)] = LpVariable(f"({v}, {w})", cat="Binary")
            es_dirigido |= (w, v) not in aristas

    prob = LpProblem("tendido_minimo", LpMinimize)
    prob += lpSum(grafo.peso_arista(v, w) * y for (v, w), y in aristas.items())

    # Acotar cantidad de aristas
    prob += lpSum(aristas.values()) == len(grafo) - 1

    # Acotar ida y vuelta si es dirigido
    if not es_dirigido:
        for (v, w), y in aristas.items():
            prob += y + aristas[(w, v)] <= 1

    # Asegurar que el grafo sea conexo
    for S in subconjuntos_de_vertices(grafo):
        aristas_dentro_de_s = []

        for v in S:
            for w in filter(lambda w: w in S, grafo.adyacentes(v)):
                aristas_dentro_de_s.append(aristas[(v, w)])

        prob += lpSum(aristas_dentro_de_s) <= len(S) - 1

    prob.solve()
    return [e for e, y in aristas.items() if value(y)]
