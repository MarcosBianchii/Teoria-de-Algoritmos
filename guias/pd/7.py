# (★★★) Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. Implementar un algoritmo que, por programación dinámica, reciba los valores y pesos de los elementos, y devuelva qué elementos deben ser guardados para maximizar la ganancia total. Indicar y justificar la complejidad del algoritmo implementado.

# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    """
    f(n, w) = max(f(n - 1, w), [f(n - 1, w - p[n]) + v[n]] if p[n] < w else 0)

    La complejidad del algoritmo es O(n * w)
    """
    def mochila_pd(n, v, p):
        # O(n * w)
        mem = [[0] * (W + 1) for _ in range(n + 1)]

        # O(n)
        for i in range(1, n + 1):
            # O(w)
            for j in range(1, W + 1):
                sin = mem[i - 1][j]
                if p[i] > j:
                    mem[i][j] = sin
                else:
                    con = mem[i - 1][j - p[i]] + v[i]
                    mem[i][j] = max(sin, con)

        return mem

    def construir_solucion(n, f, v, p):
        sol = []

        w = W  # O(n)
        for n in range(n, 0, -1):
            if f[n][w] != f[n - 1][w]:
                sol.append((v[n], p[n]))
                w -= p[n]

        # O(n)
        sol.reverse()
        return sol

    n = len(elementos)  # O(n)
    v = [0] + [v for v, _ in elementos]
    p = [0] + [p for _, p in elementos]
    f = mochila_pd(n, v, p)
    return construir_solucion(n, f, v, p)
