# (★★★) Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco. Decidió en este caso robar toda una calle en un barrio privado, que tiene la particularidad de ser circular. Gracias a los trabajos de inteligencia realizados, sabemos cuánto se puede obtener por robar en cada casa. Podemos enumerar a la primer casa como la casa 0, de la cual podríamos obtener g[0], la casa a su derecha es la 1, que nos daría g[1], y así hasta llegar a la casa n - 1, que nos daría g[n-1]. Toda casa i se considera adyacente a las casas i - 1 e i + 1. Además, como la calle es circular, la casas 0 y n - 1 también son vecinas. El problema con el que cuenta el Lunático es que sabe de experiencias anteriores que, si roba en una casa, los vecinos directos se enterarían muy rápido. No le daría tiempo a luego intentar robarles a ellos. Es decir, para robar una casa debe prescindir de robarle a sus vecinos directos. El Lunático nos encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. Dado que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a este problema. Implementar un algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles casas habría que robar, a partir de recibir un arreglo de las ganancias obtenibles. Para esto, escribir y describir la ecuación de recurrencia correspondiente. Indicar y justificar la complejidad del algoritmo propuesto.

def lunatico(ganancias):
    """
    f(0) = 0
    f(n) = max(f(n - 1), f(n - 2) + g[n])

    La complejidad del algoritmo es O(n)
    """
    if not ganancias:
        return []

    if len(ganancias) == 1:
        return [0]

    def lunatico_pd(n, g):
        # O(n)
        mem = [0] * (n + 1)

        # O(n)
        for i in range(1, n + 1):
            mem[i] = max(mem[i - 1], (mem[i - 2] or 0) + g[i])

        return mem

    def construir_solucion(n, f, g, ofs):
        sol = []
        i = n

        # O(n)
        while i > 0:
            if (f[i - 2] or 0) + g[i] > f[i - 1]:
                sol.append(i - ofs)
                i -= 2
            else:
                i -= 1

        # O(n)
        sol.reverse()
        return sol

    # O(n)
    v = [0] + ganancias[:-1]
    w = [0] + ganancias[1:]
    n = len(ganancias) - 1

    f = lunatico_pd(n, v)
    h = lunatico_pd(n, w)

    if f[-1] > h[-1]:
        return construir_solucion(n, f, v, 1)
    else:
        return construir_solucion(n, h, w, 0)
