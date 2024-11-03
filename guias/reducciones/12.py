# (★) ¿Pertenece el siguiente problema a PSPACE? Dada una lista de enteros positivos L y un entero n obtener un subconjunto de L que sume exactamente n, o, en caso de no existir, que devuelva el subconjunto de suma máxima sin superar el valor de n.

def subset_sum(L, n):
    def subset_sum_pd(n, w):
        mem = [[0] * (w + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            num = L[i - 1]
            for j in range(1, w + 1):
                sin = mem[i - 1][j]
                if num > j:
                    mem[i][j] = sin
                else:
                    con = mem[i - 1][j - num] + num
                    mem[i][j] = max(sin, con)

        return mem

    def construir_solucion(f, n, w):
        sol = []

        for i in range(n, 0, -1):
            num = L[i - 1]
            if f[i][w] != f[i - 1][w]:
                sol.append(num)
                w -= num

        sol.reverse()
        return sol

    f = subset_sum_pd(len(L), n)
    return construir_solucion(f, len(L), n)


"""
Este problema sí forma parte de PSPACE, a diferencia del problema 11, este no necesita guardar todas las soluciones posibles. Con esta implementación usando programación dinámica, podemos resolver el problema utilizando espacio pseudo-polinomial O(l * n) donde l es el largo del arreglo y n es la suma que queremos alcanzar.
"""
