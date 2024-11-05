def arnook(pedidos):
    if len(pedidos) == 0:
        return []

    pedidos.sort(key=lambda p: p[1])
    otorgados = [pedidos[0]]

    for p in pedidos:
        if otorgados[-1][1] < p[0]:
            otorgados.append(p)

    return otorgados
