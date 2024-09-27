# (★★★) Tenemos un conjunto de números v_1, v_2, ..., v_n, y queremos obtener un subconjunto de todos esos números tal que su suma sea igual o menor a un valor V, tratando de aproximarse lo más posible a V. Implementar un algoritmo que, por programación dinámica, reciba un arreglo de valores, y la suma objetivo V, y devuelva qué elementos deben ser utilizados para aproximar la suma lo más posible a V, sin pasarse. Indicar y justificar la complejidad del algoritmo implementado.

def subset_sum(elementos, v):
    """
    f(n, 0) = f(0, v) = 0
    f(n, v) = max(f(n - 1, v), [f(n - 1, v - w[n]) + w[n]] if w[n] <= v else 0)

    La complejidad del algoritmo es O(n * w)
    """
    def subset_sum_pd(n, v, w):
        # O(n)
        mem = [[0] * (v + 1) for _ in range(n + 1)]

        # O(n)
        for n in range(1, n + 1):
            # O(v)
            for v in range(1, v + 1):
                sin = mem[n - 1][v]
                if w[n] > v:
                    mem[n][v] = sin
                else:
                    con = mem[n - 1][v - w[n]] + w[n]
                    mem[n][v] = max(sin, con)

        return mem

    def construir_solucion(n, v, f, w):
        sol = []

        # O(n)
        for n in range(n, 0, -1):
            if f[n][v] != f[n - 1][v]:
                sol.append(w[n])
                v -= w[n]

        sol.reverse()
        return sol

    # O(n)
    w = [0] + elementos
    n = len(elementos)
    f = subset_sum_pd(n, v, w)
    return construir_solucion(n, v, f, w)
