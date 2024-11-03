# (★★) Definir los problemas de decisión de Grafo Bipartito y 3-Coloreo. Sabiendo que 3-Coloreo es NP-Completo, reducir Grafo Bipartito a 3-Coloreo. ¿Podemos afirmar que Grafo Bipartito es un problema NP-Completo?

"""
Problema de decisión de Grafo Bipartito:
Dado un grafo, determinar si es posible dividir el conjunto de vértices en 2 de forma tal que ningún vértice sea adyacente a ningún otro dentro del mismo subconjunto.

Problema de decisión de 3-Coloreo:
Dado un grafo, determinar si es posible dividir el conjunto de vértices en 3 de forma tal que ningún vértice sea adyacente a ningún otro dentro del mismo subconjunto.
"""


def verificador_grafo_bipartito(grafo, v1, v2):
    """
    La complejidad del algoritmo es O(V^2)
    """
    if len(v1) + len(v2) != len(grafo):
        return False

    # O(V)
    if any(v in v2 for v in v1):
        return False

    # O(V)
    if any(v in v1 for v in v2):
        return False

    # O(V^2)
    if any(w in v1 for v in v1 for w in grafo.adyacentes(v)):
        return False

    # O(V^2)
    if any(w in v2 for v in v2 for w in grafo.adyacentes(v)):
        return False

    return True


"""
Como la complejidad del verificador es polinómica, entonces Grafo Bipartito está en NP.

    def grafo_bipartito(grafo):
        # transformacion
        return 3_coloreo(grafo)

Si creamos un vértice nuevo en el grafo donde lo conectamos a todos los otros vértices entonces este nuevo vértice toma uno de los colores de los 3. Por lo que para todos los demás vértices (los originales) quedan solo 2.

Grafo Bipartito => 3-Coloreo:
Por definición si un grafo es bipartito también es 3 coloreable, pues, en el grafo nuevo vamos a poder agregar el vértice extra y colorearlo con el nuevo color que querramos incluir.

3-Coloreo => Grafo Bipartito:
Si el grafo modelado es 3 coloreable entonces, el vértice agregado tiene un color, como este es adyacente a todos los demás, todos los otros vértices tienen un color distinto a este. Como solo le quedan 2 colores para elegir al resto y pudieron ser coloreados, entonces el grafo es bipartito.
"""
