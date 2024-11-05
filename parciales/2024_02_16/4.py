from utils import peso_minimo, encontrar_camino, aristas_de_corte, actualizar_grafo_residual


def ba_sing_set(red, rios, riegos):
    red.agregar_vertice("s")
    red.agregar_vertcie("t")

    for r, capacidad in rios.items():
        red.agregar_arista("s", r, capacidad)

    for r, capacidad in riegos.items():
        red.agregar_arsita(r, "t", capacidad)

    residual, flujos = ford_fulkerson(red, "s", "t")
    corte = aristas_de_corte(red, residual, "s")
    return max(((v, w) for v, w in corte if v != "s" and w != "t"), key=lambda vw: flujos[vw])


def ford_fulkerson(red, s, t):
    residual = red.copy()
    flujos = {(v, w): 0 for v in red for w in red.adyacentes(red)}

    while (camino := encontrar_camino(residual, s, t)) is not None:
        min_cap = peso_minimo(residual, camino)
        for i in range(1, len(camino)):
            v = camino[i - 1]
            w = camino[i]

            if red.estan_unidos(v, w):
                flujos[(v, w)] += min_cap
            else:
                flujos[(v, w)] -= min_cap

            actualizar_grafo_residual(residual, v, w, min_cap)

    return residual, flujos
