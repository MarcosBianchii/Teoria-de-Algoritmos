# (★) Modificar el algoritmo anterior para que, dada una lista de enteros positivos L y un entero n, devuelva un subconjunto de L que sume exactamente n, o, en caso de no existir, que devuelva el subconjunto de suma máxima sin superar el valor de n.

def max_sumatoria_n(lista, n):
    resultado = []
    suma_maxima = 0

    def sumas(i, numeros, numsum):
        nonlocal resultado, suma_maxima
        if numsum > n:
            return

        if suma_maxima < numsum:
            resultado = numeros.copy()
            suma_maxima = numsum

        if numsum == n:
            return

        if i == len(lista):
            return

        num = lista[i]
        numeros.append(num)
        sumas(i + 1, numeros, numsum + num)

        numeros.pop()
        sumas(i + 1, numeros, numsum)

    sumas(0, [], 0)
    return resultado
