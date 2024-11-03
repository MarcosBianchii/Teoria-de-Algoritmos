# (★) Dado un tablero de ajedrez n×n, implementar un algoritmo por backtracking que ubique(si es posible) a n reinas de tal manera que ninguna pueda comerse con ninguna.

def nreinas(n):
    def validar_nreinas(reinas):
        Ui, Uj = reinas[-1]
        for i in range(len(reinas) - 1):
            Ri, Rj = reinas[i]
            # Columna
            if Rj == Uj:
                return False

            # Diagonales
            if Ri - Rj == Ui - Uj or Ri + Rj == Ui + Uj:
                return False

        return True

    def bt(i, reinas):
        if i == n:
            return reinas

        for j in range(n):
            reinas.append((i, j))
            if validar_nreinas(reinas):
                bt(i + 1, reinas)
                if len(reinas) == n:
                    return reinas

            reinas.pop()

        return reinas

    return bt(0, [])
