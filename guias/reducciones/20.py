# (★★★★) El problema de elección de caminos (Path Selection) pregunta: dado un grafo dirigido G y un set de pedidos P_1, P_2, , ...,P_c de caminos dentro de dicho grafo y un número k, ¿es posible seleccionar al menos k de esos caminos tales que ningún par de caminos seleccionados comparta ningún nodo? Demostrar que Path Selection es un problema NP-Completo. Ayuda: este problema tiene mucha semejanza con Independent Set.

"""
El problema de decisión de Path Selection es:
Dado un grafo dirigido, un conjunto de caminos y un número entero `k`, determinar si es posible seleccionar al menod k caminos tales todos sean disjuntos en sus vértices.

El problema de decisión de Independent Set es:
Dado un grafo y un número entero `k`, determinar si es posible obtener un subconjunto de vértices de tamaño a lo sumo k donde ningún vértice dentro del conjunto sea adyacente con ninguno otro también dentro de él.
"""


def verificador_path_selection(grafo, pedidos, k, elegidos):
    """
    La complejidad del algoritmo es O(l * e^2).
    """
    if len(elegidos) < k:
        return False

    # O(e)
    if any(p not in pedidos for p in elegidos):
        return False

    # O(l * e)
    conjuntos = [set(e) for e in elegidos]

    # O(l * e^2)
    for i in range(len(elegidos)):
        for j in range(i + 1, len(conjuntos)):
            if any(v in conjuntos[j] for v in elegidos[i]):
                return False

    return True


"""
Como la complejidad del verificador es polinómica, Path Selection está en NP.

    def independent_set(grafo, k):
        # transformacion
        return path_selection(grafo, pedidos, k)

Creamos un grafo donde por cada arista del grafo original, existe un vértice que la represente en el grafo modelo, vamos a conectar a todos los vértices con todos. Para el conjuntos de caminos pedidos vamos a, por cada vértice del grafo original, crear un camino que pase por todos sus vértices arista que sean adyacentes a él.

IS => PS:
Teniendo en cuenta que existe un Independent Set de a lo sumo tamaño k en el grafo original. Esto significa que hay k caminos pedidos disjuntos. Esto es porque dos caminos son disjuntos sii sus respectivos vértices no son adyacentes, pues, si lo fueran, ambos compartirían al vértice arista que los conectan en sus caminos. Entonces se dá Path Selection de a lo sumo k caminos.

PS => IS:
Teniendo k caminos disjuntos, esto significa que de cada camino podemos contar a su vértice representante del grafo original. Como son disjuntos los caminos, estos vértices son independientes, pues no hay otro vértice representante que comparta ninguna de sus aristas adyacentes. 
"""
