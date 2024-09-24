# (★★★) Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. Además, cada charla tiene asociado un valor de ganancia. Implementar un algoritmo que, utilizando programación dinámica, reciba un arreglo que en cada posición tenga una charla representada por una tripla de inicio, fin y valor de cada charla, e indique cuáles son las charlas a dar para maximizar la ganancia total obtenida. Indicar y justificar la complejidad del algoritmo implementado.

def scheduling(charlas):
    """
    f(0) = 0
    f(n) = max(v[n] + f(p[n]), f(n - 1))

    La complejidad del algoritmo es O(nlogn)
    """
    # O(nlogn)
    charlas.sort(key=lambda ch: ch[1])

    def encontrar_no_superpuesta(i):
        if i == 0:
            return 0

        def se_superponen(i, j):
            return charlas[i][1] > charlas[j][0]

        def busqueda_binaria(a, b):
            if b - a == 1:
                return a + 1 if not se_superponen(a, i) else 0

            mid = (a + b) // 2
            if not se_superponen(mid, i):
                a = mid
            else:
                b = mid

            return busqueda_binaria(a, b)

        return busqueda_binaria(0, i)

    def scheduling_pd(n, p, v):
        # O(n)
        mem = [0] * (n + 1)

        # O(n)
        for i in range(1, n + 1):
            mem[i] = max(v[i] + mem[p[i]], mem[i - 1])

        return mem

    def construir_solucion(n, f, p, v):
        sol = []

        # O(n)
        while n > 0:
            if v[n] + f[p[n]] >= f[n - 1]:
                sol.append(charlas[n - 1])
                n = p[n]
            else:
                n -= 1

        sol.reverse()
        return sol

    n = len(charlas)  # O(nlogn)
    p = [0] + [encontrar_no_superpuesta(i) for i in range(n)]
    v = [0] + [ch[2] for ch in charlas]
    f = scheduling_pd(n, p, v)
    return construir_solucion(n, f, p, v)
