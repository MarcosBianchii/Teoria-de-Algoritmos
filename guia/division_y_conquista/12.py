# (★★★) Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, tal que la cantidad total de elementos del arreglo es potencia de 2 (por ende, n también lo es). Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma que quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, sin utilizar espacio adicional (obviando el utilizado por la recursividad). Indicar y justificar su complejidad temporal.

# Pista: Pensar primero cómo habría que hacer si el arreglo tuviera 4 elementos({C1, C2, D1, D2}). Luego, pensar a partir de allí el caso de 8 elementos, etc… para encontrar el patrón.

# [C1, C2,   D1, D2] -> [C1, D1, C2, D2]
# [C1, C2], [D1, D2]
# [C1, C2,   D1, D2]
# [C1, D1,   C2, D2]

# [C1, C2,   C3, C4,   D1, D2,   D3, D4] -> [C1, D1, C2, D2, C3, D3, C4, D4]
# [C1, C2,   C3, C4], [D1, D2,   D3, D4]
# [C1, C2], [C3, C4], [D1, D2], [D3, D4]

# [C1, C2,   C3, C4], [D1, D2,   D3, D4]
# [C1, C3,   C2, C4], [D1, D3,   D2, D4]

#

# [C1, C2, C3, C4, C5, C6, C7, C8, D1, D2, D3, D4, D5, D6, D7, D8] -> [C1, D1, C2, D2, C3, D3, C4, D4, C5, D5, C6, D6, C7, D7, C8, D8]


def alternar(arr):
    def merge(a, mid, b):
        return -1

    def split(a, b):
        if b - a > 1:
            mid = (a + b) // 2
            split(a, mid)
            split(mid, b)
            merge(a, mid, b)

    return split(0, len(arr))


arr = [0, 2, 4, 6, 1, 3, 5, 7]
print(alternar(arr))
