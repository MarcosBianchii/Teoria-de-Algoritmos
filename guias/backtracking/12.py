# (★) Modificar el algoritmo anterior para que, dada una lista de enteros positivos L y un entero n, devuelva un subconjunto de L que sume exactamente n, o, en caso de no existir, que devuelva el subconjunto de suma máxima sin superar el valor de n.

def max_sumatoria_n(L, n):
    def bt(i, optimo, suma_opt, subset, suma):
        if i == len(L):
            return (subset.copy(), suma) if suma > suma_opt else (optimo, suma_opt)

        subset.append(L[i])
        if suma + L[i] <= n:
            optimo, suma_opt = bt(i + 1, optimo, suma_opt, subset, suma + L[i])
            if suma_opt == n:
                return optimo, suma_opt

        subset.pop()
        return bt(i + 1, optimo, suma_opt, subset, suma)

    return bt(0, [], 0, [], 0)[0]
