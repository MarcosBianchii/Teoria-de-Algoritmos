# (★★) Implementar el algoritmo de Ford-Fulkerson, asumiendo que ya está implementada una función actualizar_grafo_residual, definida como actualizar_grafo_residual(grafo_residual, u, v, valor), que recibe el grafo residual, una arista dirigida dada por los vértices u y v, y el nuevo valor del flujo a través de la arista (u,v) y actualiza el grafo residual ya teniendo en cuenta el peso anterior de la arista, y su antiparalela. Devolver un diccionario con los valores de los flujos para todas las aristas del grafo original.

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

        for w in residual.adyacentes(v):
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


def peso_minimo(residual, p):
    return min(residual.peso_arista(p[i - 1], p[i]) for i in range(len(p)))


def ford_fulkerson(red, s, t):
    """
    La complejidad del algoritmo es O(v * a^2)
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
