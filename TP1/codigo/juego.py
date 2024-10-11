def elegir_moneda(monedas, cmp, a, b):
    if cmp(monedas[a], monedas[b]):
        moneda = monedas[a]
        a += 1
    else:
        moneda = monedas[b]
        b -= 1

    return moneda, a, b


def jugar(monedas):
    valor_sophia = 0
    valor_mateo = 0

    primera = 0
    ultima = len(monedas) - 1

    while primera <= ultima:
        moneda, primera, ultima = elegir_moneda(monedas, lambda x, y: x > y, primera, ultima)
        valor_sophia += moneda

        if primera > ultima:
            break

        moneda, primera, ultima = elegir_moneda(monedas, lambda x, y: x < y, primera, ultima)
        valor_mateo += moneda

    return valor_sophia, valor_mateo
