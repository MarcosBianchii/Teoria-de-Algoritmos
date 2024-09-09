# (★) Se tiene un arreglo de N >= 3 elementos en forma de pico, esto es: estrictamente creciente hasta una determinada posición p, y estrictamente decreciente a partir de ella(con 0 < p < N−1). Por ejemplo, en el arreglo[1, 2, 3, 1, 0, -2] la posición del pico es p = 2. Se pide: a. Implementar un algoritmo de división y conquista de orden O(logn) que encuentre la posición p del pico. b. Justificar el orden del algoritmo mediante el teorema maestro.

def posicion_pico(v, ini, fin):
    """
    T(n) = aT(n/b) + O(n^c)

    a = 1
    b = 2
    c = 0

    log_b(a) = c -> T(n) = O(n^c logn) = O(logn)
    """
    mid = (ini + fin) >> 1

    anterior = v[mid - 1]
    elemento = v[mid]
    siguiente = v[mid + 1]

    if anterior < elemento and elemento > siguiente:
        return mid

    if anterior < elemento:
        ini = mid
    elif elemento > siguiente:
        fin = mid

    return posicion_pico(v, ini, fin)
