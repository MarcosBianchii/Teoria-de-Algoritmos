# (★★) Se tiene un sistema monetario(ejemplo, el nuestro). Se quiere dar “cambio” de una determinada cantidad de plata. Se desea devolver el cambio pedido, usando la mínima cantidad de monedas/billetes. Implementar un algoritmo que, por programación dinámica, reciba un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, y devuelva qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizda. Indicar y justificar la complejidad del algoritmo implementado.

def cambio(monedas, monto):
    """
    f(0) = 0
    f(n) = 1 + min(f(n - m) for m in monedas if m <= n)

    La complejidad del algoritmo es O(n * m)
    """
    def cambio_pd(n):
        # O(n)
        mem = [0] * (n + 1)

        # O(n)
        for n in range(1, n + 1):
            # O(m)
            mem[n] = 1 + min(mem[n - m] for m in monedas if m <= n)

        return mem

    def construir_solucion(f, n):
        sol = []

        # O(n)
        while n > 0:
            minimo = n
            moneda = 1  # O(m)
            for m in monedas:
                if m <= n and f[n - m] < minimo:
                    minimo = f[n - m]
                    moneda = m

            n -= moneda
            sol.append(moneda)

        # O(n)
        sol.reverse()
        return sol

    f = cambio_pd(monto)
    return construir_solucion(f, monto)
