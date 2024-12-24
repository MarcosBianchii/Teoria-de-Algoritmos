
def jugar(monedas):
    """
    f(0, s) = 0
    f(1, s) = m[s]
    f(2, s) = max(m[s], m[s + 1])
    f(n, s):
        pm = m[s] + f(n - 2, s + 1 + (m[s + 1] > m[s + n - 1]))
        um = m[s + n - 1] + f(n - 2, s + (m[s] > m[s + i - 2]))
        return max(pm, um)

    La complejidad del algoritmo es O(n^2)
    """
    def jugar_pd(n, m):
        # O(n^2)
        mem = [[0] * (n - i + 1) for i in range(n + 1)]
        mem[1] = m

        # O(n)
        for s in range(n - 1):
            mem[2][s] = max(m[s], m[s + 1])

        # O(n^2)
        for i in range(3, n + 1):
            for s in range(n - i + 1):
                pm = m[s] + mem[i - 2][s + 1 + (m[s + 1] > m[s + i - 1])]
                um = m[s + i - 1] + mem[i - 2][s + (m[s] > m[s + i - 2])]
                mem[i][s] = max(pm, um)

        return mem

    def construir_solucion(n, f, m):
        mateo = 0
        sol = []

        s = 0  # O(n)
        for i in range(n, 0, -2):
            # Sophia
            if i >= 2:
                pm = m[s] + f[i - 2][s + 1 + (m[s + 1] > m[s + i - 1])]
                um = m[s + i - 1] + f[i - 2][s + (m[s] > m[s + i - 2])]
            else:
                pm = um = m[s]

            if pm > um:
                sol.append(f"Sophia debe agarrar la primera ({m[s]})")
                s += 1
            else:
                sol.append(f"Sophia debe agarrar la ultima ({m[s + i - 1]})")

            if i == 1:
                break

            # Mateo
            pm = m[s]
            um = m[s + (i - 1) - 1]
            if pm > um:
                sol.append(f"Mateo agarra la primera ({pm})")
                s += 1
            else:
                sol.append(f"Mateo agarra la ultima ({um})")

            mateo += max(pm, um)

        return f[n][0], mateo, sol

    n = len(monedas)
    f = jugar_pd(n, monedas)
    return construir_solucion(n, f, monedas)
