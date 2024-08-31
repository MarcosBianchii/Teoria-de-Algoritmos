# (★) Se tiene un arreglo en el que se registran los resultados de tests automáticos de una porción de código. Este código se encontraba funcionando pero, debido a unos cambios que se están realizando, en algún momento dejó de funcionar. Se registra un 1 si pasa los tests, 0 en caso contrario. De esta manera, el arreglo tendrá la forma [1, 1, 1, ..., 0, 0, ...] (es decir, unos seguidos de ceros). Se pide: a. una función de orden O(logn) que, por división y conquista, encuentre el índice del primer 0, de forma que se pueda reconocer rápidamente en qué modificación del código se dejó de pasar los tests. Si no hay ningún 0 (solo hay unos), debe devolver -1. b. demostrar con el Teorema Maestro que la función es, en efecto, O(logn).

# Ejemplos:

# [1, 1, 0, 0, 0] →  2
# [0, 0, 0, 0, 0] →  0
# [1, 1, 1, 1, 1] → -1

def indice_primer_cero(arr):
    """
    T(n) = aT(n/b) + O(n^c)

    a = 1
    b = 2
    c = 0

    log_b(a) = c -> T(n) es O(n^c logn) = O(logn)
    """
    a, b = 0, len(arr)
    while a < b:
        mid = (a + b) >> 1
        if arr[mid - 1] == 1 and arr[mid] == 0:
            return mid

        if arr[mid] == 1:
            a = mid + 1
        elif arr[mid] == 0:
            b = mid

    return a if a < len(arr) else -1
