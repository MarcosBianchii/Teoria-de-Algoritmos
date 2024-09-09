# (★) Se tiene un sistema monetario(ejemplo, el nuestro). Se quiere dar “cambio” de una determinada cantidad de plata. Implementar un algoritmo Greedy que devuelva el cambio pedido, usando la mínima cantidad de monedas/billetes. El algoritmo recibirá un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, y debe devolver qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizada. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar si es óptimo, o dar un contraejemplo. ¿Por qué se trata de un algoritmo Greedy? Justificar

def cambio(monedas, monto):
    """
    Este algoritmo no siempre encuentra la solucion optima. Un contra ejemplo es
        - monedas: [1, 2, 6, 9, 11]
        - monto: 15

    Donde la solucion optima es [9, 6] pero este algoritmo encuentra [11, 2, 2].

    El algoritmo es greedy porque aplica una regla sencilla de forma iterativa
    llevando el estado actual al estado optimo local esperando llegar al optimo general.
    Como esta mostrado arriba no siempre lo alcanza.

    La complejidad del algoritmo es O(monto)
    """
    suma_de_plata = 0
    pago = []

    # O(n)
    for moneda in reversed(monedas):
        while suma_de_plata + moneda <= monto:
            suma_de_plata += moneda
            pago.append(moneda)

    return pago
