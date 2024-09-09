# (★★★★) Resolver el ejercicio anterior, por división y conquista, en orden O(n), dada la misma aclaración. Justificar el orden de la solución.

"""
T(n) = aT(n/b) + O(n^c)

CASO 1: Hacer 1 llamada recursiva y O(n) por cada llamada
    a = 1, b > 1, c = 1
    log_b(a) < c -> T(n) = O(n^c) = O(n)

CASO 2: Hacer 2 llamadas recursivas y O(1) por cada llamada
    a = 2, b > 1, c = 0
    log_b(a) > c -> T(n) = O(n^log_b(a)) = O(n)

"""


def mas_de_la_mitad(arr):
    """
    T(n) = aT(n/b) + O(n^c)

    a = 1
    b = 2
    c = 1

    log_b(a) < c -> T(n) = O(n^c) = O(n)
    """
    def pares(arr):
        for i in range(0, len(arr) - 1, 2):
            yield arr[i], arr[i + 1]

    def mas_de_la_mitad_rec(arr):
        if len(arr) == 0:
            return None

        if len(arr) == 1:
            return arr[0]

        mitad = []
        for x0, x1 in pares(arr):
            if x0 == x1:
                mitad.append(x0)

        m1 = mas_de_la_mitad_rec(mitad)
        if m1 and arr.count(m1) > len(arr) // 2:
            return m1

        m2 = arr[-1] if len(arr) % 2 == 1 else None
        if m2 and arr.count(m2) > len(arr) // 2:
            return m2

        return None

    return mas_de_la_mitad_rec(arr)
