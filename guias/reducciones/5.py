# (★) Para cada uno de los siguientes problemas, implementar un verificador polinomial y justificar su complejidad.

# a. Dado un número por parámetro, si es la solución al problema de búsqueda del máximo en un arreglo.

def verificador_busqueda_del_maximo(arr, k):
    """
    La complejidad del verificador es O(n)
    """
    # O(n)
    existe = False
    for x in arr:
        if x > k:
            return False

        existe |= x == k

    return existe


# b. Dado un arreglo, si es la solución a tener el arreglo ordenado.

def verificador_arreglo_ordenado(arr):
    """
    La complejidad del verificador es O(n)
    """
    # O(n)
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False

    return True


# c. Dadas un arreglo de posiciones de Reinas, si es la solución de colocar al menos N-reinas en un tablero NxN.

def verificador_n_reinas(reinas, n):
    """
    La complejidad del verificador es O(n^2)
    """
    if len(reinas) != n:
        return False

    # O(n)
    for i in range(n):
        r0 = reinas[i]  # O(n)
        for j in range(i + 1, n):
            r1 = reinas[j]

            if r0[0] == r1[0] or r0[1] == r1[1]:
                return False

            if r0[0] - r0[1] == r1[0] - r1[1]:
                return False

            if r0[0] + r0[1] == r1[0] + r1[1]:
                return False

    return True
