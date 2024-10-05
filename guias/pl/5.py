# (★) Implementar un modelo de programación lineal que resuelva el problema de 3-SAT mínimo: que encuentre una solución que satisfaga, utlizando la menor cantidad de variables en true posible.

from pulp import LpProblem, LpVariable, LpMinimize, lpSum, value
prob = LpProblem("min_3sat", LpMinimize)


def OR(x, y):
    global prob
    res = LpVariable(f"({x.getName()} | {y.getName()})", cat="Binary")
    prob += res == x + y
    return res


def AND(x, y):
    global prob
    res = LpVariable(f"({x.getName()} & {y.getName()})", cat="Binary")
    prob += res <= x
    prob += res <= y
    prob += res == x + y - 1
    return res


def NOT(x):
    global prob
    res = LpVariable(f"!{x.getName()}", cat="Binary")
    prob += res == 1 - x
    return res


def min_3sat(n, expression):
    global prob
    ys = [LpVariable(f"x{i}", cat="Binary") for i in range(n)]

    prob += lpSum(ys)
    prob += expression(*ys) == 1

    prob.solve()
    return [bool(value(y)) for y in ys]


print(min_3sat(3, lambda x, y, z: OR(AND(x, z), AND(y, z))))
