# (★) Escribir un algoritmo que, utilizando backtracking, dada una lista de enteros positivos L y un entero n devuelva todos los subconjuntos de L que suman exactamente n.

def sumatorias_n(L, n):
    def sumas(i, resultados, numeros, suma):
        if suma == n:
            resultados.append(numeros.copy())

        if suma >= n or i == len(L):
            return resultados

        numeros.append(L[i])
        sumas(i + 1, resultados, numeros, suma + L[i])

        numeros.pop()
        return sumas(i + 1, resultados, numeros, suma)

    return sumas(0, [], [], 0)
