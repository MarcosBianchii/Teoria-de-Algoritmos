# (★★★) Dado un arreglo de n enteros (no olvidar que pueden haber números negativos), encontrar el subarreglo contiguo de máxima suma, utilizando División y Conquista. Indicar y justificar la complejidad del algoritmo. Ejemplos:

# [5, 3, 2, 4, -1]  → [5, 3, 2, 4]
# [5, 3, -5, 4, -1] → [5, 3]
# [5, -4, 2, 4, -1] → [5, -4, 2, 4]
# [5, -4, 2, 4]     → [5, -4, 2, 4]

# [5,   3,   2,   4,   -1] → [5, 3, 2, 4]
# [5,   3], [2,   4,   -1]
# [5], [3], [2], [4,   -1]
# [5,   3], [2], [4], [-1]
# [5,   3], [2], [4]
# [5,   3], [2,   4]
# [5,   3,   2,   4]

# [5,   3,   -5,   4,   -1] → [5, 3]
# [5,   3], [-5,   4,   -1]
# [5], [3], [-5], [4,   -1]
# [5,   3], [-5], [4], [-1]
# [5,   3], [-5], [4]
# [5,   3],       [4]
# [5,   3]


# [5,   -4,   2,   4,   -1] → [5, -4, 2, 4]
# [5,   -4], [2,   4,   -1]
# [5], [-4], [2], [4,   -1]
# [5],       [2], [4], [-1]
# [5],       [2], [4]
# [5],       [2,   4]
# [5,   -4,   2,   4]


# [5,   -4,   2,   4] → [5, -4, 2, 4]
# [5,   -4], [2,   4]
# [5], [-4], [2], [4]
# [5],       [2,   4]
# [5,   -4,   2,   4]

# [-3,   4,   -1,   2,   1,   -5,   4] → [4, -1, 2, 1]
# [-3,   4,   -1], [2,   1,   -5,   4]
# [-3], [4,   -1], [2,   1], [-5,   4]
# [-3], [4], [-1], [2], [1], [-5], [4]
# [-3], [4],       [2,   1],       [4]
#       [4],       [2,   1],       [4]
#       [4],                       [4]
#       [4,   -1,   2,   1]

from math import inf


def max_subarray(arr):
    """
    T(n) = aT(n/b) + O(n^c)

    a = 2
    b = 2
    c = 1

    log_b(a) = c -> T(n) = O(n^c logn) = O(nlogn)
    """
    def suma(a, b):
        return sum(arr[i] for i in range(a, b))

    def expandir_suma(start, end, step):
        suma_parcial = 0
        suma = -inf
        res = start
        for i in range(start, end, step):
            suma_parcial += arr[i]
            if suma_parcial > suma:
                suma = suma_parcial
                res = i

        return res, suma

    def max_suma_medio(a, mid, b):
        am, suma_izq = expandir_suma(mid - 1, a - 1, -1)
        bm, suma_der = expandir_suma(mid, b, 1)
        bm += 1  # El rango es exclusivo

        suma_mid = suma(am, bm)
        suma_max = max(suma_izq, suma_mid, suma_der)
        if suma_izq == suma_max:
            return am, mid
        if suma_mid == suma_max:
            return am, bm
        if suma_der == suma_max:
            return mid, bm

    def max_subarray_rec(a, b):
        if b - a == 1:
            return a, b

        mid = (a + b) // 2
        al, bl = max_subarray_rec(a, mid)
        suma_izq = suma(al, bl)

        am, bm = max_suma_medio(a, mid, b)
        suma_mid = suma(am, bm)

        ar, br = max_subarray_rec(mid, b)
        suma_der = suma(ar, br)

        suma_max = max(suma_izq, suma_mid, suma_der)
        if suma_izq == suma_max:
            return al, bl
        if suma_mid == suma_max:
            return am, bm
        if suma_der == suma_max:
            return ar, br

    a, b = max_subarray_rec(0, len(arr))
    return arr[a:b]
