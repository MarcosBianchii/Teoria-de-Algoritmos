# (★) Implementar un modelo de programación lineal que resuelva el Problema de la Mochila de valor máximo (ejercicio 7 de PD).

from pulp import LpVariable, LpProblem, LpMaximize, lpSum, value


def mochila(elementos, W):
    ys = [LpVariable(f"y{i}", cat="Binary") for i in range(len(elementos))]

    prob = LpProblem("mochila", LpMaximize)
    prob += lpSum(y * w for (_, w), y in zip(elementos, ys)) <= W
    prob += lpSum(y * v for (v, _), y in zip(elementos, ys))

    prob.solve()
    return [x for i, x in enumerate(elementos) if value(ys[i])]
