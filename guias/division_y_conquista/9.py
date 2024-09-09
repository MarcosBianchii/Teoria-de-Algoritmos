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

    def numero_que_mas_aparece(a, b):
        if b - a == 1:
            return arr[a], 1

        mid = (a + b) // 2
        nl, cl = numero_que_mas_aparece(a, mid)
        nr, cr = numero_que_mas_aparece(mid, b)

        cr += contar_numero_en_intervalo(nr, a, mid)
        cl += contar_numero_en_intervalo(nl, mid, b)

        if cl > cr:
            return nl, cl
        else:
            return nr, cr

    _, apariciones = numero_que_mas_aparece(0, len(arr))
    return apariciones > len(arr) / 2
