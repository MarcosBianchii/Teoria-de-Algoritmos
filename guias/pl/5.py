# (★) Implementar un modelo de programación lineal que resuelva el problema de 3-SAT mínimo: que encuentre una solución que satisfaga, utlizando la menor cantidad de variables en true posible.

from pulp import LpProblem, LpVariable, LpMinimize, lpSum, value


def min_sat(clausuras):
    ys = {}  # O(n)
    for clausura in clausuras:
        for x in clausura:
            absx = abs(x)
            if absx not in ys:
                ys[absx] = LpVariable(str(absx), cat="Binary")

    prob = LpProblem("min SAT", LpMinimize)
    prob += lpSum(ys.values())

    # O(n)
    for clausura in clausuras:
        prob += lpSum(ys[x] if x > 0 else 1 - ys[-x] for x in clausura) >= 1

    prob.solve()
    return [x for x, y in ys.items() if bool(value(y))]
