# (★) Implementar un modelo de programación lineal que resuelva el problema de Vertex Cover mínimo (ejercicio 13 de BT).

from pulp import LpProblem, LpVariable, LpMinimize, value, lpSum


def vertex_cover_min(grafo):
    ys = {v: LpVariable(str(v), cat="Binary") for v in grafo}

    problem = LpProblem("vertex_cover_min", LpMinimize)
    problem += lpSum(ys.values())

    for v in grafo:
        ady = grafo.adyacentes(v)
        problem += ys[v] + lpSum(ys[w] for w in ady) >= len(ady) * (1 - ys[v])

    problem.solve()
    return [v for v, y in ys.items() if value(y)]
