# (★) Implementar un algoritmo de multiplicación de dos números grandes de longitud n, por división y conquista, con un orden de complejidad mejor que O(n ^ 2). Justificar el orden del algoritmo mediante el teorema maestro.

def multiplicar(a, b):
    """
    T(n) = aT(n/b) + O(n^c)

    a = 3
    b = 2
    c = 1

    log_b(a) > c -> T(n) = O(n^log_b(a)) = O(n^1.6)
    """
    def karatsuba_offman(x, y, n):
        if n <= 1:
            mul = 0
            for _ in range(y):
                mul += x
            return mul

        half_len = n // 2
        mask = (1 << half_len) - 1

        x0 = x & mask
        x1 = (x & ~mask) >> half_len
        y0 = y & mask
        y1 = (y & ~mask) >> half_len

        next_n = n >> 1
        p = karatsuba_offman(x0 + x1, y0 + y1, next_n)
        x0y0 = karatsuba_offman(x0, y0, next_n)
        x1y1 = karatsuba_offman(x1, y1, next_n)
        return (x1y1 << n) + ((p - x1y1 - x0y0) << half_len) + x0y0

    return karatsuba_offman(a, b, 64)
