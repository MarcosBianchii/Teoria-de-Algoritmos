# (★★★) Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, tal que la cantidad total de elementos del arreglo es potencia de 2 (por ende, n también lo es). Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma que quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, sin utilizar espacio adicional (obviando el utilizado por la recursividad). Indicar y justificar su complejidad temporal.

# Pista: Pensar primero cómo habría que hacer si el arreglo tuviera 4 elementos ({C1, C2, D1, D2}). Luego, pensar a partir de allí el caso de 8 elementos, etc… para encontrar el patrón.

def alternar(arr):
    """
    T(n) = aT(n/b) + O(n^c)

    a = 2
    b = 2
    c = 1

    log_b(a) = c -> T(n) = O(n^c logn) = O(nlogn)
    """
    def alternar_rec(a, b):
        if b - a >= 4:
            mid = (a + b) // 2
            alternar_rec(a, mid)
            alternar_rec(mid, b)

            for i in range(0, mid - a, 2):
                arr[a + i + 1], arr[mid + i] = arr[mid + i], arr[a + i + 1]

    alternar_rec(0, len(arr))
    return arr

# [1, 3,   2, 4]
# [1, 3], [2, 4]
# [1, 2,   3, 4]


print(alternar([1, 3, 2, 4]))

# [1, 3,   5, 7,   2, 4,   6, 8]
# [1, 3,   5, 7], [2, 4,   6, 8]
# [1, 3], [5, 7], [2, 4], [6, 8]
# [1, 5,   3, 7], [2, 6,   4, 8]
# [1, 2,   3, 4,   5, 6,   7, 8]

print(alternar([1, 3, 5, 7, 2, 4, 6, 8]))
