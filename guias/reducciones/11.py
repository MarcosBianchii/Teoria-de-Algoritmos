# (★) ¿Pertenece el siguiente problema a PSPACE? Dada una lista de enteros positivos L y un entero n obtener todos los subconjuntos de L que suman exactamente n.

def subconjuntos(L, n):
    def dfs(i, subset, suma):
        if suma > n:
            return []

        if suma == n:
            return [subset]

        if i == len(L):
            return []

        izq = dfs(i + 1, subset + [L[i]], suma + L[i])
        der = dfs(i + 1, subset, suma)
        return izq + der

    return dfs(0, [], 0)


"""
Este problema no forma parte de PSPACE porque por la naturaleza del problema, es necesario guardar una cantidad exponencial de soluciones. El problema en cuestión es el problema NP-Completo Subset Sum con la salvedad de que ahora no buscamos una solución sino que todas, esto implica recorrer todas las posibilidades y las soluciones crecen de forma exponencial.
"""
