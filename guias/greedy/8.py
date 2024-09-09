# (★★) Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. Implementar un algoritmo Greedy que, reciba dos arreglos de valores y pesos de los elementos, y devuelva qué elementos deben ser guardados para maximizar la ganancia total. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar

# ¿Qué diferencias se perciben si en vez de tener que colocar los elementos completos, se pueden fraccionar para nuestra conveniencia?

# Cada elemento i de la forma (valor, peso)

def mochila(elementos, W):
    """
    Este algoritmo no siempre encuentra la solucion optima. Un contra ejemplo es
        - elementos: [(2, 1), (5, 5)]
        - W: 5

    Donde la solucion optima es [(5, 5)] pero este algoritmo encuentra [(2, 1)]. Esto es
    porque prioriza la relacion valor/peso de los elementos y no toma en cuenta que aunque
    tenga buen valor/peso tenga mal valor y punto.

    El algoritmo es Greedy porque en cada iteracion intenta maximizar el valor y minimizar el
    peso del proximo elemento que esta por guardar en la mochila, esa es la regla sencilla. Esto
    se repite esperando que resuelva el problema de forma optima.

    La complejidad del algoritmo es O(nlogn)
    """
    # O(nlogn)
    elementos.sort(key=lambda e: e[0] / e[1], reverse=True)

    # O(n)
    mochila = []
    peso_mochila = 0
    for e, w in elementos:
        if peso_mochila + w <= W:
            peso_mochila += w
            mochila.append((e, w))

    return mochila
