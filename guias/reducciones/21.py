# (★★★) El problema de selección de caminos (Path Selection) pregunta: dado un grafo dirigido G y un set de pedidos P_1, P_2, ..., P_c de caminos dentro de dicho grafo y un número k, ¿es posible seleccionar al menos k de esos caminos tales que ningún par de caminos seleccionados comparta ningún nodo? Dato: Path Selection es un problema NP-Completo. Ahora bien, queremos demostrar nuevamente (pero de otra forma a la vista en clase) que Independent Set es un problema NP-Completo. Demostrar que Independent Set es un problema NP-Completo, utilizando Path Selection para esto.

def verificador_independent_set(grafo, k, iset):
    """
    La complejidad del verificador es O(S + E)
    """
    if len(iset) < k:
        return False

    # O(S)
    if any(v not in grafo for v in iset):
        return False

    # O(S + E)
    if any(w in iset for v in iset for w in grafo.adyacentes(v)):
        return False

    return True


"""
Como la complejidad del verificador es polinómica, Independent Set está en NP.

    def path_selection(grafo, pedidos, k):
        # transformacion
        return independent_set(grafo, k)

Creamos un nuevo grafo, donde cada uno de los caminos sea un vértice, por cada camino vamos a chequear cuales comparten vértices, en ese caso creamos una arista entre ellos.

PS => IS:
Si sabemos que podemos tomar k caminos tales que entre ellos son disjuntos, entonces en el grafo modelo, como nosotros por cada camino creamos un vértice y este es adyacente a todos los otros caminos no disjuntos, esto significa que vamos a tener k vértices no adyacentes en el grafo modelo, osea, un conjunto independiente de tamaño k.

IS => PS:
Si sabemos que existe un conjunto independiente en el grafo modelo de tamaño k, como cada uno es adyacente sii los caminos representantes de ellos comparten vértices, esto quiere decir que un par de vértices no adyacentes en el grafo modelo representan 2 caminos disjuntos. Si pudimos determinar que existe un conjunto independiente de tamaño k en el grafo modelo, entonces tenemos k caminos disjuntos en el grafo original dados por el arreglo de pedidos.
"""
