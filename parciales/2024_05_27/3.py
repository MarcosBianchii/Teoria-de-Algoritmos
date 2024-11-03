from pulp import LpVariable, LpProblem, LpMinimize, lpSum, value


def dominating_set(grafo, valores):
    ys = {v: LpVariable(str(v), cat="Binary") for v in grafo}

    prob = LpProblem("Dominating Set", LpMinimize)
    prob += lpSum(valores[v] * y for v, y in ys.items())
    for v in grafo:
        prob += ys[v] + lpSum(ys[w] for w in grafo.adyacentes(v)) >= 1

    prob.solve()
    return [v for v, y in ys.items() if value(y)]
