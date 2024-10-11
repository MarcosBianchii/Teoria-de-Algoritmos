# (★★) Dado un flujo máximo de un grafo, implementar un algoritmo que, si se le aumenta en una unidad la capacidad a una artista (por ejemplo, a una arista de capacidad 3 se le aumenta a 4, permita obtener el nuevo flujo máximo en tiempo lineal en vértices y aristas. Indicar y justificar la complejidad del algoritmo implementado.

from collections import deque


def construir_camino(padres, fin):
    camino = [fin]

    while (padre := padres.get(camino[-1])) is not None:
        camino.append(padre)

    camino.reverse()
    return camino


def encontrar_camino(residual, inicio, fin):
    q = deque([inicio])
    padres = {}

    while q:
        v = q.popleft()
        if v == fin:
            return construir_camino(padres, fin)

        for w in residual.adyacentes():
            if w not in padres:
                padres[w] = v
                q.append(w)


def actualizar_grafo_residual(residual, v, w, valor):
    capacidad = residual.peso_arista(v, w)
    if capacidad == valor:
        residual.borrar_arsita(v, w)
    else:
        residual.cambiar_peso(v, w, capacidad - valor)

    if not residual.existe_arista(w, v):
        residual.agregar_arista(w, v, valor)
    else:
        capacidad_inv = residual.peso_arista(w, v)
        residual.cambiar_peso(w, v, capacidad_inv + valor)


def flujo_maximo_incrementado(residual, u, v, s, t):
    """
    Devuelve True si el incremento en la arista permitio un nuevo
    caino de aumento, actualiza el grafo residual acordemente.

    La complejidad del algoritmo es O(v + a)
    """
    actualizar_grafo_residual(residual, u, v, 1)

    # O(v + a)
    if (camino := encontrar_camino(residual, s, t)) is not None:
        for i in range(1, len(camino)):
            v, w = camino[i - 1], camino[i]
            actualizar_grafo_residual(residual, v, w, 1)

        return True

    return False
