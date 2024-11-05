def laboratorio(farmacos, catalogo, L):
    farmacos.sort(reverse=True, key=lambda f: catalogo[f[0]])
    mochila = []
    ocupado = 0

    for nombre, cantidad in farmacos:
        tomado = min(cantidad, L - ocupado)
        if tomado == 0:
            break

        mochila.append((nombre, tomado))
        ocupado += tomado

    return mochila
