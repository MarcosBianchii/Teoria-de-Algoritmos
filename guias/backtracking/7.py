# (★) Implementar un algoritmo de backtracking que, dado una pieza de caballo en un tablero de ajedrez, determine los movimientos a realizar para que el caballo logre pasar por todos los casilleros del tablero una única vez. Recordar que el caballo mueve en forma de L (dos casilleros en una dirección, y un casillero en forma perpendicular).

def knight_tour(n):
    V = n ** 2
    offsets = [
        (-2, -1), (-2, 1), (-1, 2), (1, 2),
        (2, 1), (2, -1), (-1, -2), (1, -2),
    ]

    def en_rango(v):
        i, j = v
        return i >= 0 and j >= 0 and i < n and j < n

    def adyacentes(v):
        i, j = v
        for Oi, Oj in offsets:
            yield i + Oi, j + Oj

    def existe_hamilton(v, visitados):
        if len(visitados) == V:
            return True

        for w in filter(en_rango, adyacentes(v)):
            if w not in visitados:
                visitados.add(w)

                if existe_hamilton(w, visitados):
                    return True

                visitados.remove(w)

        return False

    for i in range(n):
        for j in range(n):
            v = (i, j)
            if existe_hamilton(v, set([v])):
                return True

    return False
