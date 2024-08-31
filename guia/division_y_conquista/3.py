# (★) Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada de un número n, en tiempo O(logn). Por ejemplo, para n = 10 debe devolver 3, y para n = 25 debe devolver 5. Justificar el orden del algoritmo.

def parte_entera_raiz(n):
    """
    T(n) = aT(n/b) + O(n^c)

    a = 1
    b = 2
    c = 0

    log_b(a) = c -> T(n) = O(n^c logn) = O(logn)
    """
    def busqueda_binaria(a, b):
        mid = (a + b) >> 1
        square = mid ** 2

        if square <= n and n < (mid + 1) ** 2:
            return mid

        if square < n:
            a = mid + 1
        elif square > n:
            b = mid

        return busqueda_binaria(a, b)

    return busqueda_binaria(0, n)
