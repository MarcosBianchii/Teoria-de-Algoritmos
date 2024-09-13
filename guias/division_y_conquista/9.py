# (★★★) Implementar una función, que utilice división y conquista, de orden O(nlogn) que dado un arreglo de n números enteros devuelva true o false según si existe algún elemento que aparezca más de la mitad de las veces. Justificar el orden de la solución. Ejemplos:

# [1, 2, 1, 2, 3]    -> false
# [1, 1, 2, 3]       -> false
# [1, 2, 3, 1, 1, 1] -> true
# [1]                -> true


def mas_de_la_mitad(arr):
    """
    T(n) = aT(n/b) + O(n^c)

    a = 2
    b = 2
    c = 1

    log_b(a) = c -> T(n) = O(n^c logn) = O(nlogn)
    """
    def contar_numero_en_intervalo(n, a, b):
        count = 0
        for i in range(a, b):
            if arr[i] == n:
                count += 1

        return count

    def mas_de_la_mitad_rec(a, b):
        if b - a == 1:
            return arr[a]

        mid = (a + b) // 2
        izq = mas_de_la_mitad_rec(a, mid)
        der = mas_de_la_mitad_rec(mid, b)

        izq = contar_numero_en_intervalo(izq, a, mid)
        der = contar_numero_en_intervalo(der, mid, b)
        mitad_largo = (b - a) / 2

        if izq > mitad_largo:
            return izq
        if der > mitad_largo:
            return der

        return None

    return mas_de_la_mitad_rec(0, len(arr)) != None
