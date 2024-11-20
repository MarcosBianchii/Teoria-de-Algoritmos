from pulp import LpProblem, LpVariable, LpMaximize, value


def max_clique(grafo):
    ys = {v: LpVariable(str(v), cat="Binary") for v in grafo}
    prob = LpProblem("Max Clique", LpMaximize)

    for v in grafo:
        for w in grafo:
            if v != w and not grafo.estan_unidos(v, w):
                prob += ys[v] + ys[w] <= 1

    prob.solve()
    return [v for v, y in ys.items() if value(y)]
