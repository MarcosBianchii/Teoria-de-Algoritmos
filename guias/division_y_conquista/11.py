# (★★★★) Implementar una función, que utilice división y conquista, de orden O(n) que dado un arreglo de n números enteros devuelva true o false según si existe algún elemento que aparezca más de dos tercios de las veces. Justificar el orden de la solución.


def mas_de_dos_tercios(arr):
    """
    T(n) = aT(n/b) + O(n^c)

    a = 1
    b = 3
    c = 1

    log_b(a) < c -> T(n) = O(n^c) = O(n)
    """
    def tripletes(arr):
        for i in range(0, len(arr) - 2, 3):
            yield arr[i], arr[i + 1], arr[i + 2]

    def mas_de_dos_tercios_rec(arr):
        if len(arr) == 0:
            return None

        if len(arr) == 1:
            return arr[0]

        dos_tercios = []
        for x0, x1, x2 in tripletes(arr):
            if x0 == x1 and x1 == x2:
                dos_tercios.append(x1)

        k = 2 * len(arr) // 3
        m1 = mas_de_dos_tercios_rec(dos_tercios)
        if m1 and arr.count(m1) > k:
            return m1

        resto = len(arr) % 3
        m2 = arr[-1] if resto == 1 else None
        if m2 and arr.count(m2) > k:
            return m2

        m3 = arr[-2] if resto == 2 else None
        if m3 and arr.count(m3) > k:
            return m3

        return None

    return mas_de_dos_tercios_rec(arr) != None
