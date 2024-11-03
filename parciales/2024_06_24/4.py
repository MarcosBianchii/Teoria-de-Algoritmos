def potencia(b, n):
    if n == 1:
        return b

    pot = potencia(b, n // 2) ** 2
    if n % 2 == 0:
        return pot
    else:
        return pot * b
