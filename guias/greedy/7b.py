# (★★) En Wakanda, tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. Cada día podemos y debemos comprar uno(y sólo uno) de los productos, pero Wakanda está atravesando una era de deflación y los precios disminuyen todo el tiempo. El precio del producto i el día j+1 es exactamente la mitad del precio en el día j. El arreglo R[i] indica todos los precios del primer día. Si bien para reducir costos se debería esperar a que los productos sigan bajando, los tiempos de entrega no nos permiten esperar, y cada día debemos comprar uno de los productos.

# Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar


def precios_deflacion(R):
    """
    El algoritmo es optimo porque espera que los precios siempre esten mas baratos el dia de mañana
    que hoy. Si esto cambiara en algun momento podria no siempre encontrar la solucion optima. Compra
    los productos de forma ascendente en precio, por lo que los mas caros siempre los va a comprar al
    final donde ya van a haber bajado mas de precio que si los hubiera comprado al principio.

    El algoritmo es Greedy porque de forma iterativa aplica una regla simple, esta siendo comprar el
    producto mas barato ahora y dejar que los demas bajen de precio mañana. Repite esta regla esperando
    que de forma local solucionar de forma optima el problema general.

    La complejidad del algoritmo es O(nlogn)
    """
    # O(nlogn)
    R.sort()

    # O(n)
    costo = 0
    for i in range(len(R)):
        costo += R[i] / 2 ** i

    return costo
