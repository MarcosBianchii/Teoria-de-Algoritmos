# (★) Dado un tablero de ajedrez n×n, implementar un algoritmo por backtracking que ubique(si es posible) a n reinas de tal manera que ninguna pueda comerse con ninguna.

def nreinas(n):
    reinas = []

    def espacio_libre(i, j):
        for Ri, Rj in reinas:
            # Columna
            if Rj == j:
                return False

            # Diagonales
            if Ri - Rj == i - j or Ri + Rj == i + j:
                return False

        return True

    def nreinas_rec(i):
        if i == n:
            return True

        for j in range(n):
            if espacio_libre(i, j):
                reinas.append((i, j))
                if nreinas_rec(i + 1):
                    return True

                reinas.pop()

        return False

    nreinas_rec(0)
    return reinas
