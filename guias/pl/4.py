# (★) Implementar un modelo de programación lineal que resuelva el problema de Dominating Set mínimo (ejercicio 14 de BT).

from pulp import LpProblem, LpVariable, LpMinimize, lpSum, value


def dominating_set_min(grafo):
    ys = {v: LpVariable(str(v), cat="Binary") for v in grafo}

    prob = LpProblem("dominating_set_min", LpMinimize)
    prob += lpSum(ys.values())

    for v in grafo:
        prob += ys[v] + lpSum(ys[w] for w in grafo.adyacentes(v)) >= 1

    prob.solve()
    return [v for v, y in ys.items() if value(y)]
