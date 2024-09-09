# (★★) Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos. Implementar un algoritmo Greedy que dé la cantidad mínima de faros que se necesitan para que todos los submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”). Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado da siempre la solución óptima? Justificar.

# devolver una lista de faros. Cada faro debe ser una tupla con su posición en (x,y)
# matriz booleana, indica True en las posiciones con submarinos

RADIO = 2


def submarinos(matriz):
    """
    Este algoritmo no siempre encuentra la solucion optima. Un contra ejemplo es

    matriz: [
        [True,  False, False, False, False, False, False, False, False,  True],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, True,   True, False, False, False, False],
        [False, False, False, False, True,   True, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [True,  False, False, False, False, False, False, False, False,  True],
    ]

    Donde la solucion optima es [(2, 2), (7, 2), (2, 7), (7, 7)] pero este
    algoritmo encuentra [(3, 3), (9, 0), (0, 0), (9, 9), (0, 9)].

    La complejidad del algoritmo es O(n * m)
    """
    if len(matriz) == 0:
        return []

    n = len(matriz)
    m = len(matriz[0])

    # O(n * m)
    submarinos = set()
    for i in range(n):
        for j in range(m):
            if matriz[i][j]:
                submarinos.add((i, j))

    def plano_de_rango_2(i, j):
        # O(1)
        Ai, Bi = max(i - RADIO, 0), min(i + RADIO + 1, n)
        Aj, Bj = max(j - RADIO, 0), min(j + RADIO + 1, m)

        # O(1)
        for i in range(Ai, Bi):
            for j in range(Aj, Bj):
                yield (i, j)

    def colectar_submarinos(Si, Sj):
        # O(1)
        encontrados = []
        for i, j in plano_de_rango_2(Si, Sj):
            if (i, j) in submarinos:
                encontrados.append((i, j))

        return encontrados

    # O(n * m)
    faros = []
    while len(submarinos) > 0:
        Si, Sj = submarinos.pop()
        submarinos_por_iluminar = []
        mejor_faro = Si, Sj

        # O(1)
        for i, j in plano_de_rango_2(Si, Sj):
            propuesta = colectar_submarinos(i, j)
            if len(submarinos_por_iluminar) < len(propuesta):
                submarinos_por_iluminar = propuesta
                mejor_faro = i, j

        # O(1)
        faros.append(mejor_faro)
        for submarino in submarinos_por_iluminar:
            submarinos.remove(submarino)

    return faros
