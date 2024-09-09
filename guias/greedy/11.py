# (★★) Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se rompen. Implementar un algoritmo greedy que, teniendo una lista de pesos de n pesos comprados, encuentre la mejor forma de distribuir los productos en la menor cantidad posible de bolsas. Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y para una lista con los pesos: [4, 2, 1, 3, 5]. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. Indicar y justificar la complejidad del algoritmo implementado.

def bolsas(capacidad, productos):
    """
    Este algoritmo no siempre encuentra la solucion optima. Un contra ejemplo es
        - capacidad: 10
        - productos: [5, 6, 4, 5]

    Donde la solucion optima es [[6, 4], [5, 5]] pero este algoritmo encuentra [[5, 4], [6], [5]]. Si
    ordenara los productos por peso de forma descendente antes de aplicar el algoritmo entonces para
    este caso en particular encuentra la solucion optima.

    La complejidad del algoritmo es O(n^2)
    """
    if not productos:
        return []

    # O(n)
    bolsas = [[]]
    for peso in productos:
        # O(n)
        bolsa = min(bolsas, key=sum)
        if sum(bolsa) + peso <= capacidad:
            bolsa.append(peso)
        else:
            bolsas.append([peso])

    return bolsas
