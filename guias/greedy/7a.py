# (★★) Tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. Cada día podemos y debemos comprar uno(y sólo uno) de los productos, pero vivimos en una era de inflación y los precios aumentan todo el tiempo. El precio del producto i el día j es R[i]^(j+1) (j comenzando en 0). Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar ¿Qué modificaciones se deben realizar para un estado de deflación, con productos que bajan de precio todo el tiempo?

def precios_inflacion(R):
    """
    El algoritmo siempre encuentra la solucion optima, compra los productos mas caros
    antes de que estos suban de precio de forma exponencial. El dia en el que los precios
    van a estar mas baratos es hoy. Priorizando los productos mas caros primero conseguimos
    minimizar el costo total.

    El algoritmo es Greedy porque dada la informacion que tiene en el momento aplica una regla
    sencilla para acercarse a la solucion mas optima posible esperando llegar a la solucion
    optima del problema.

    En este caso intenta comprar lo mas caro esperando que a futuro este todavia mas caro, de
    esta forma minimizando el coste a futuro siempre. Consigue encontrar la solucion optima
    porque sabe que los precios solamente van a subir, si hubiera algun tipo de deflacion implicada
    en cierto punto entonces este algoritmo no lo esperaria y no llegaria a una solucion optima.

    Para productos que siempre bajan de precio, habria que ordenar el arreglo de forma ascendente. Lo
    demas puede quedar de la misma forma.

    La complejidad del algoritmo es O(nlogn)
    """
    # O(nlogn)
    R.sort(reverse=True)

    # O(n)
    costo = 0
    for i in range(len(R)):
        costo += R[i] ** (i + 1)

    return costo
