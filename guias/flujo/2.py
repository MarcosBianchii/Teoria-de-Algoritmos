# (★★) Implementar el algoritmo de Ford-Fulkerson, asumiendo que ya está implementada una función actualizar_grafo_residual, definida como actualizar_grafo_residual(grafo_residual, u, v, valor), que recibe el grafo residual, una arista dirigida dada por los vértices u y v, y el nuevo valor del flujo a través de la arista (u,v) y actualiza el grafo residual ya teniendo en cuenta el peso anterior de la arista, y su antiparalela. Devolver un diccionario con los valores de los flujos para todas las aristas del grafo original.

from utils import encontrar_camino, peso_minimo, actualizar_grafo_residual


def ford_fulkerson(red, s, t):
    """
    La complejidad del algoritmo es O(V * A^2)
    """
    flujos = {(v, w): 0 for v in red for w in red.adyacentes(v)}
    residual = red.copy()

    while (camino := encontrar_camino(residual, s, t)) is not None:
        min_cap = peso_minimo(residual, camino)

        for i in range(1, len(min_cap)):
            v, w = camino[i - 1], camino[i]

            if red.estan_unidos(v, w):
                flujos[(v, w)] += min_cap
            else:
                flujos[(v, w)] -= min_cap

            actualizar_grafo_residual(residual, v, w, min_cap)

    return flujos
