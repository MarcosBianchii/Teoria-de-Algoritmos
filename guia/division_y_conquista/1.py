# (★) Implementar, por división y conquista, una función que dado un arreglo sin elementos repetidos y casi ordenado (todos los elementos se encuentran ordenados, salvo uno), obtenga el elemento fuera de lugar. Indicar y justificar su complejidad temporal.

def elemento_desordenado(arr):
    """
    T(n) = aT(n/b) + O(n^c)

    a = 2
    b = 2
    c = 0

    log_b(a) > c -> T(n) = O(n^log_2(2)) = O(n)
    """
    def dfs(a, b):
        if a < b:
            mid = (a + b) >> 1
            if (m := max(arr[a], arr[mid], arr[b])) != arr[b]:
                return m

            if arr[mid] > arr[mid + 1]:
                return arr[mid]

            if l := dfs(a, mid):
                return l
            if r := dfs(mid + 1, b):
                return r

    return dfs(0, len(arr) - 1)
