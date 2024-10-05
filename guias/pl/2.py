# (★) Implementar un modelo de programación lineal que resuelva el problema de Juan El Vago (ejercicio 4 de PD).

from pulp import LpProblem, LpMaximize, LpVariable, lpSum, value


def juan_el_vago(trabajos):
    n = len(trabajos)
    ys = [LpVariable(f"y{i}", cat="Binary") for i in range(n)]

    prob = LpProblem("juan_el_vago", LpMaximize)
    prob += lpSum(ys[i] * trabajos[i] for i in range(n))
    for i in range(0, n - 1):
        prob += ys[i] + ys[i + 1] <= 1

    prob.solve()
    return [i for i in range(n) if value(ys[i])]
