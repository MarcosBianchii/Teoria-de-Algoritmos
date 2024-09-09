# (★) Dada una matriz de 9x9, implementar un algoritmo por backtracking que llene la matriz con números del 1 al 9, dadas las condiciones del Sudoku (si es posible). Las condiciones son: (i) Las celdas están dispuestas en 9 subgrupos de 3x3. (ii) Cada columna y cada fila no puede repetir número. (iii) Cada subgrupo de 3x3 no puede repetir número.

def resolver_sudoku(matriz):
    def verificar_celda(fila, col, num):
        for x in range(9):
            if matriz[fila][x] == num:
                return False

            if matriz[x][col] == num:
                return False

        fila = fila - fila % 3
        col = col - col % 3
        for i in range(fila, fila + 3):
            for j in range(col, col + 3):
                if matriz[i][j] == num:
                    return False

        return True

    def resolver(fila, col):
        if col == 9:
            fila += 1
            col = 0

        if fila == 9:
            return True

        if matriz[fila][col] != 0:
            return resolver(fila, col + 1)

        for i in range(1, 10):
            if verificar_celda(fila, col, i):
                matriz[fila][col] = i
                if resolver(fila, col + 1):
                    return True

        matriz[fila][col] = 0
        return False

    resolver(0, 0)
    return matriz
