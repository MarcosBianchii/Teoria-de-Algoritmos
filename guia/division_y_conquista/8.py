# (★) Dados un conjunto de n elementos, y 2 arreglos de longitud n, con dichos elementos. El arreglo A está completamente ordenado de menor a mayor. El arreglo B se encuentra desordenado. Indicar, por división y conquista, la cantidad de inversiones necesarias al arreglo B para que quede ordenado de menor a mayor, con un orden de complejidad mejor que O(n^2). Justificar el orden del algoritmo mediante el teorema maestro.

def contar_inversiones(A, B):
    """
    T(n) = aT(n/b) + O(n^c)

    a = 2
    b = 2
    c = 1

    log_b(a) = c -> T(n) = O(n^c logn) = O(nlogn)
    """
    translate = {x: i for i, x in enumerate(A)}
    B = [translate[x] for x in B]

    def merge(a, mid, b):
        arr1 = B[a:mid]
        arr2 = B[mid:b]
        i = 0
        j = 0
        k = a
        inversions = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                B[k] = arr1[i]
                i += 1
            else:
                inversions += len(arr1) - i
                B[k] = arr2[j]
                j += 1

            k += 1

        while i < len(arr1):
            B[k] = arr1[i]
            i += 1
            k += 1

        while j < len(arr2):
            B[k] = arr2[j]
            j += 1
            k += 1

        return inversions

    def split(a, b):
        if b - a == 1:
            return 0

        mid = (a + b) // 2
        l = split(a, mid)
        r = split(mid, b)
        return l + r + merge(a, mid, b)

    return split(0, len(B))
