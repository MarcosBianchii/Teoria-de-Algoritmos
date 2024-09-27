# (★★★) Manejamos un negocio que atiende clientes en Londres y en California. Nos interesa cada mes decidir si operar en una u otra ciudad. Los costos de operación para cada mes pueden variar y son dados por 2 arreglos: L y C, con valores para todos los meses hasta n. Naturalmente, si en un mes operamos en una ciudad, y al siguiente en una distinta, habrá un costo fijo M por la mudanza. Dados los arreglos de costos de operación en Londres(L) y California(C), indicar la secuencia de las n localizaciones en las que operar durante los n meses, sabiendo que queremos minimizar el total de los costos de operación. Se puede empezar en cualquier ciudad. Indicar y justificar la complejidad del algoritmo implementado.

def plan_operativo(L, C, M):
    """
    f(0) = 0
    g(0) = 0
    f(n) = min(f(n - 1), g(n - 1) + m) + f(n)
    g(n) = min(g(n - 1), f(n - 1) + m) + g(n)

    La complejidad del algoritmo es O(n)
    """
    def plan_operativo_pd(n, l, c):
        # O(n)
        lon = [0] * (n + 1)
        cal = [0] * (n + 1)

        # O(n)
        for n in range(1, n + 1):
            lon[n] = min(lon[n - 1], cal[n - 1] + M) + l[n]
            cal[n] = min(cal[n - 1], lon[n - 1] + M) + c[n]

        return lon, cal

    def construir_solucion(n, lon, cal):
        i = 0 if lon[n] < cal[n] else 1
        f = [lon, cal]
        sol = []

        # O(n)
        for n in range(n, 0, -1):
            sol.append("londres" if i == 0 else "california")

            if f[1 - i][n - 1] + M < f[i][n - 1]:
                i = 1 - i

        # O(n)
        sol.reverse()
        return sol

    n = len(L)  # O(n)
    l, c = [0] + L, [0] + C
    lon, cal = plan_operativo_pd(n, l, c)
    return construir_solucion(n, lon, cal)
