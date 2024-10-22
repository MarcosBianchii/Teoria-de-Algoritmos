# (★★★) Carlitos (primo de Juan, el vago) trabaja para una empresa de publicidad. Tiene un determinado presupuesto P que no puede sobrepasar, y tiene que una serie de campañas publicitarias para elegir. La campaña i cuesta C_i. También se han realizado diversos estudios que permiten estimar cuánta ganancia nos dará cada campaña, que denominaremos G_i. Implementar un algoritmo que reciba esta información y devuelva cuáles campañas debe realizar Carlitos. Indicar y justificar la complejidad del algoritmo propuesto. ¿Da lo mismo si los valores están expresados en pesos argentinos, dólares u otra moneda? Por ejemplo, si una campaña cuesta 100 dólares, para pasar a pesos se debe hacer la conversión de divisa.

# cada campaña publicitaria i de la forma (Gi, Ci)
def carlitos(c_publicitaria, P):
    """
    f(n, 0) = f(0, p) = 0
    f(n, p) = max(f(n - 1, p), [f(n - 1, p - c[n]) + g[n]] if c[n] <= p else 0)

    La complejidad del algoritmo es O(n * 2^m) donde m es la cantidad de bits de P
    """
    def carlitos_pd(n, g, c):
        # O(n * p)
        mem = [[0] * (P + 1) for _ in range(n + 1)]

        # O(n)
        for n in range(1, n + 1):
            # O(p)
            for p in range(1, P + 1):
                sin = mem[n - 1][p]
                if c[n] > p:
                    mem[n][p] = sin
                else:
                    con = mem[n - 1][p - c[n]] + g[n]
                    mem[n][p] = max(sin, con)

        return mem

    def construir_solucion(n, f, g, c):
        sol = []

        p = P  # O(n)
        for n in range(n, 0, -1):
            if f[n][p] != f[n - 1][p]:
                sol.append((g[n], c[n]))
                p -= c[n]

        # O(n)
        sol.reverse()
        return sol

    n = len(c_publicitaria)  # O(n)
    g = [0] + [g for g, _ in c_publicitaria]
    c = [0] + [c for _, c in c_publicitaria]
    f = carlitos_pd(n, g, c)
    return construir_solucion(n, f, g, c)
