# (★★) Dado un flujo máximo de un grafo, implementar un algoritmo que, si se le aumenta en una unidad la capacidad a una artista (por ejemplo, a una arista de capacidad 3 se le aumenta a 4, permita obtener el nuevo flujo máximo en tiempo lineal en vértices y aristas. Indicar y justificar la complejidad del algoritmo implementado.

from utils import encontrar_camino, actualizar_grafo_residual


def flujo_maximo_incrementado(red, u, v, s, t):
    """
    Devuelve True si el incremento en la arista permitio un nuevo
    caino de aumento, actualiza el grafo red acordemente.

    La complejidad del algoritmo es O(v + a)
    """
    actualizar_grafo_residual(red, u, v, 1)

    # O(v + a)
    if (camino := encontrar_camino(red, s, t)) is not None:
        for i in range(1, len(camino)):
            v, w = camino[i - 1], camino[i]
            actualizar_grafo_residual(red, v, w, 1)

        return True

    return False
