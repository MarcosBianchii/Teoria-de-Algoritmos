from collections import deque


def construir_camino(padres, fin):
    camino = [fin]

    # O(v)
    while (padre := padres[camino[-1]]) is not None:
        camino.append(padre)

    # O(v)
    camino.reverse()
    return camino


def encontrar_camino(red, s, t):
    """
    BFS: La complejidad es O(v + e)
    """
    padres = {s: None}
    q = deque([s])

    while q:
        v = q.popleft()
        if v == t:
            return construir_camino(padres, t)

        for w in red.adyacentes(v):
            if w not in padres:
                padres[w] = v
                q.append(w)


def peso_minimo(residual, p):
    return min(residual.peso_arista(p[i - 1], p[i]) for i in range(1, len(p)))


def aristas_de_corte(red, residual, s):
    visitados = set([s])
    stack = [s]

    while stack:
        v = s.pop()
        for w in residual.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                stack.append(w)

    corte = set()
    for v in visitados:
        for w in red.adyacentes(v):
            if w not in visitados:
                corte.add((v, w))

    return corte


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
