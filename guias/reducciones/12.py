# (★) ¿Pertenece el siguiente problema a PSPACE? Dada una lista de enteros positivos L y un entero n obtener un subconjunto de L que sume exactamente n, o, en caso de no existir, que devuelva el subconjunto de suma máxima sin superar el valor de n.

def subset_sum(L, n):
    def bt(i, opt, opt_suma, parcial, suma):
        if i == len(L):
            return (parcial.copy(), suma) if suma > opt_suma else (opt, opt_suma)

        parcial.append(L[i])
        if suma + L[i] <= n:
            opt, opt_suma = bt(i + 1, opt, opt_suma, parcial, suma + L[i])
            if opt_suma == n:
                return opt, opt_suma

        parcial.pop()
        return bt(i + 1, opt, opt_suma, parcial, suma)

    return bt(0, [], 0, [], 0)


"""
Este problema forma parte de PSPACE, a diferencia del problema 11, este no necesita guardar todas las soluciones posibles. Con esta implementación por backtracking, podemos resolver el problema utilizando espacio polinomial O(l) siendo l la cantidad de elementos de L.
"""
