# (★★) Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, pero no quiere trabajar dos días seguidos. Dado un arreglo con el monto esperado a ganar cada día, determinar, por programación dinámica, el máximo monto a ganar, sabiendo que no aceptará trabajar dos días seguidos. Hacer una reconstrucción para verificar qué días debe trabajar. Indicar y justificar la complejidad del algoritmo implementado.

def juan_el_vago(trabajos):
    """
    f(0) = 0
    f(n) = max(f(n - 1), f(n - 2) + v[n])

    La complejidad del algoritmo es O(n)
    """
    def juan_el_vago_pd(n, v):
        # O(n)
        mem = [0] * (n + 1)

        # O(n)
        for i in range(1, n + 1):
            mem[i] = max(mem[i - 1], (mem[i - 2] or 0) + v[i])

        return mem

    def construir_solucion(f, n, v):
        sol = []

        # O(n)
        while n > 0:
            if (f[n - 2] or 0) + v[n] > f[n - 1]:
                sol.append(n - 1)
                n -= 2
            else:
                n -= 1

        # O(n)
        sol.reverse()
        return sol

    n = len(trabajos)
    v = [0] + trabajos
    f = juan_el_vago_pd(n, v)
    return construir_solucion(f, n, v)
