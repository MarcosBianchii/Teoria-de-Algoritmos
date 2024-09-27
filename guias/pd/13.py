# (★★★) Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse. Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos). Indicar y justificar la complejidad del algoritmo.

def bodegon_dinamico(P, W):
    """
    f(n, 0) = f(0, w) = 0
    f(n, w) = max(f(n - 1, w), [f(n - 1, w - p[n]) + p[n]] if p[n] < w else 0)

    La complejidad del algoritmo es O(n * w)
    """
    def bodegon_pd(n, p):
        # O(n * w)
        mem = [[0] * (W + 1) for _ in range(n + 1)]

        # O(n)
        for n in range(1, n + 1):
            # O(w)
            for w in range(1, W + 1):
                sin = mem[n - 1][w]
                if p[n] > w:
                    mem[n][w] = sin
                else:
                    con = mem[n - 1][w - p[n]] + p[n]
                    mem[n][w] = max(sin, con)

        return mem

    def construir_solucion(n, f, p):
        sol = []

        w = W  # O(n)
        for n in range(n, 0, -1):
            if f[n][w] != f[n - 1][w]:
                sol.append(p[n])
                w -= p[n]

        # O(n)
        sol.reverse()
        return sol

    # O(n)
    p = [0] + P
    n = len(P)
    f = bodegon_pd(n, p)
    return construir_solucion(n, f, p)
