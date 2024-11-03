from pulp import LpVariable, LpProblem, lpSum, LpMinimize


def sat(clausulas):
    ys = {}
    for c in clausulas:
        for v in c:
            absv = abs(v)
            if absv not in ys:
                ys[absv] = LpVariable(str(absv), cat="Binary")

    prob = LpProblem("3-SAT", LpMinimize)
    prob += lpSum(ys.values())

    for c in clausulas:
        prob += lpSum(ys[v] if v > 0 else 1 - ys[-v] for v in c) >= 1

    prob.solve()
    return prob.valid()
