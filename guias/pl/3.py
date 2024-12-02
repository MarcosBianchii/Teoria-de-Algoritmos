# (★) Implementar un modelo de programación lineal que resuelva el problema de Vertex Cover mínimo (ejercicio 13 de BT).

from pulp import LpProblem, LpVariable, LpMinimize, value, lpSum


def vertex_cover_min(grafo):
    ys = {v: LpVariable(str(v), cat="Binary") for v in grafo}

    prob = LpProblem("vertex_cover_min", LpMinimize)
    prob += lpSum(ys.values())

    for v in grafo:
        ady = grafo.adyacentes(v)
        prob += (1 - ys[v]) * len(ady) <= lpSum(ys[w] for w in ady)

    prob.solve()
    return [v for v, y in ys.items() if value(y)]
