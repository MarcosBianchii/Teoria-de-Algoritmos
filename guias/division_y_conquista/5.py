# (★) Implementar Merge Sort. Justificar el orden del algoritmo mediante el teorema maestro.

def merge_sort(arr):
    """
    T(n) = aT(n/b) + O(n^c)

    a = 2
    b = 2
    c = 1

    log_b(a) = c -> T(n) = O(n^c logn) = O(nlogn)
    """
    def merge(a, mid, b):
        arr1 = arr[a:mid]
        arr2 = arr[mid:b]
        i = 0
        j = 0
        k = a

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                arr[k] = arr1[i]
                i += 1
            else:
                arr[k] = arr2[j]
                j += 1

            k += 1

        while i < len(arr1):
            arr[k] = arr1[i]
            i += 1
            k += 1

        while j < len(arr2):
            arr[k] = arr2[j]
            j += 1
            k += 1

    def split(a, b):
        if b - a > 1:
            mid = (a + b) >> 1
            split(a, mid)
            split(mid, b)
            merge(a, mid, b)

    split(0, len(arr))
    return arr


if __name__ == "__main__":
    arr = [3, 5, 4, 2, 1]
    merge_sort(arr)
    print(arr)
