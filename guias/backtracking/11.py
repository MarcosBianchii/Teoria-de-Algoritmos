# (★) Escribir un algoritmo que, utilizando backtracking, dada una lista de enteros positivos L y un entero n devuelva todos los subconjuntos de L que suman exactamente n.

def sumatorias_n(lista, n):
    resultados = []

    def sumas(i, numeros, suma_parcial):
        if suma_parcial == n:
            resultados.append(numeros.copy())
            return

        if suma_parcial > n:
            return

        if i == len(lista):
            return

        num = lista[i]
        numeros.append(num)
        sumas(i + 1, numeros, suma_parcial + num)

        numeros.pop()
        sumas(i + 1, numeros, suma_parcial)

    sumas(0, [], 0)
    return resultados
