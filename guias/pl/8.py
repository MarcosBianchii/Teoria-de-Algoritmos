# (★★) Implementar un modelo de programación lineal que determine la cantidad mínima de colores a utilizar para poder pintar a un grafo de colores, de tal forma que ningún adyacente comparta color entre sí.

from pulp import LpProblem, LpVariable, LpMinimize, lpSum


def min_coloreo(grafo):
    def colorear(n):
        vs = {v: [LpVariable(f"{v}_{k}", cat="Binary")
                  for k in range(n)] for v in grafo}

        prob = LpProblem("k-coloreo", LpMinimize)
        prob += lpSum(vs[v][k] for k in range(n) for v in grafo)

        for v in grafo:
            prob += lpSum(vs[v]) == 1

            for w in grafo.adyacentes(v):
                for k in range(n):
                    prob += vs[v][k] + vs[w][k] <= 1

        prob.solve()
        return prob.valid()

    def busqueda_binaria(a, b):
        if b - a == 1:
            return a if colorear(a) else a + 1

        mid = (a + b) // 2
        if not colorear(mid):
            a = mid
        else:
            b = mid

        return busqueda_binaria(a, b)

    return busqueda_binaria(0, len(grafo) + 1)
