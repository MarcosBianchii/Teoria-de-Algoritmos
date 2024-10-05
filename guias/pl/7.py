# (★★) Implementar un modelo de programación lineal que resuelva el problema de Independent Set Máximo (ejercicio 4 de BT).

from pulp import LpProblem, LpVariable, lpSum, LpMaximize, value


def independent_set(grafo):
    ys = {v: LpVariable(str(v), cat="Binary") for v in grafo}

    prob = LpProblem("independent set maximo", LpMaximize)
    prob += lpSum(ys.values())

    M = len(grafo) + 1
    for v in grafo:
        prob += ys[v] + lpSum(ys[w] for w in grafo.adyacentes(v)) <= 1 + M * (1 - ys[v])

    prob.solve()
    return [v for v, y in ys.items() if value(y)]
