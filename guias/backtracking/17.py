# (★★★) Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos. Implementar un algoritmo que dé la cantidad mínima de faros que se necesitan para que todos los submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”).


# devolver una lista de faros. Cada faro debe ser una tupla con su posición en (x, y)
# matriz booleana, indica True en las posiciones con submarinos
def submarinos(matriz):
    if not matriz:
        return []

    n = len(matriz)
    m = len(matriz[0])

    submarinos = set()
    for i in range(n):
        for j in range(m):
            if matriz[i][j]:
                submarinos.add((i, j))

    def plano_de_rango_2(i, j):
        Ai, Bi = max(i - 2, 0), min(i + 3, n)
        Aj, Bj = max(j - 2, 0), min(j + 3, m)

        for i in range(Ai, Bi):
            for j in range(Aj, Bj):
                yield i, j

    def colectar_submarinos(Fi, Fj):
        iluminados = set()
        for i, j in plano_de_rango_2(Fi, Fj):
            if (i, j) in submarinos:
                iluminados.add((i, j))
                submarinos.remove((i, j))

        return iluminados

    def iluminar_submarinos(faros):
        nonlocal submarinos

        if not submarinos:
            return faros.copy()

        min_faros = None
        Si, Sj = submarinos.pop()
        for i, j in plano_de_rango_2(Si, Sj):
            extras = colectar_submarinos(i, j)
            faros.append((i, j))

            propuesta = iluminar_submarinos(faros)
            if min_faros == None:
                min_faros = propuesta
            else:
                min_faros = min(min_faros, propuesta, key=len)

            submarinos |= extras
            faros.pop()

        submarinos.add((Si, Sj))
        return min_faros

    return iluminar_submarinos([])
