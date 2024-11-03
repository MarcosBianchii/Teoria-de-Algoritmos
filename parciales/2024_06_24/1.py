from pulp import LpProblem, LpVariable, LpMaximize, lpSum, value


def juan_no_tan_vago(trabajos):
    ys = [LpVariable(str(i), cat="Binary") for i in range(len(trabajos))]

    prob = LpProblem("Juan no tan vago", LpMaximize)
    prob += lpSum(x * y for x, y in zip(trabajos, ys))

    for i in range(len(ys) - 2):
        prob += ys[i] + ys[i + 1] + ys[i + 2] <= 2

    prob.solve()
    return [i for i in range(len(ys)) if value(ys[i])]
