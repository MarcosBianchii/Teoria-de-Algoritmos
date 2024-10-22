# (★★) Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar desde 0 a K, siendo que las operaciones posibles son:

# (i) aumentar el valor del operando en 1;

# (ii) duplicar el valor del operando.

# Implementar un algoritmo que, por programación dinámica, obtenga la menor cantidad de operaciones a realizar (y cuáles son dichas operaciones). Desarrollar la ecuación de recurrencia. Indicar y justificar la complejidad del algoritmo implementado. Aclaración: asegurarse de que el algoritmo presentado sea de programación dinámica, con su correspondiente ecuación de recurrencia.

def operaciones(k):
    """
    f(n) = min(f(n // 2) + n % 2, f(n - 1)) + 1

    La complejidad del algoritmo es O(2^m) donde m es la cantidad de bits de k
    """
    def operaciones_pd(k):
        mem = [0] * (k + 1)

        # O(k)
        for i in range(1, k + 1):
            mem[i] = min(mem[i // 2] + i % 2, mem[i - 1]) + 1

        return mem

    def construir_solucion(f, k):
        sol = []

        # O(k)
        while k > 0:
            if f[k // 2] + k % 2 < f[k - 1]:
                sol.append("por2")
                k //= 2
            else:
                sol.append("mas1")
                k -= 1

        # O(k)
        sol.reverse()
        return sol

    f = operaciones_pd(k)
    return construir_solucion(f, k)
