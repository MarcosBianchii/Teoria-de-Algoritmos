# (★★★★) El problema de elección de caminos (Path Selection) pregunta: dado un grafo dirigido G y un set de pedidos P_1, P_2, , ...,P_c de caminos dentro de dicho grafo y un número k, ¿es posible seleccionar al menos k de esos caminos tales que ningún par de caminos seleccionados comparta ningún nodo? Demostrar que Path Selection es un problema NP-Completo. Ayuda: este problema tiene mucha semejanza con Independent Set.

"""
El problema de decisión de Path Selection es:
Dado un grafo dirigido, un conjunto de caminos y un número entero `k`, determinar si es posible seleccionar al menod k caminos tales todos sean disjuntos en sus vértices.

El problema de decisión de Independent Set es:
Dado un grafo y un número entero `k`, determinar si es posible obtener un subconjunto de vértices de tamaño a lo sumo k donde ningún vértice dentro del conjunto sea adyacente con ninguno otro también dentro de él.
"""


def verificador_path_selection(grafo, pedidos, k, elegidos):
    """
    La complejidad del algoritmo es O(l * e^2) donde l es el largo del camino más largo.
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

Creamos un nuevo grafo con los mismos vértices, por cada arista del grafo original creamos un nuevo vértice y los unimos con sus vértices correspondientes mediante un par de arcos antiparalelos. Para el conjunto de caminos pedidos vamos a, por cada vértice `v` crear un camino donde por cada adyacente vayamos y volvamos de forma que quede algo por el estilo de: [v, v-u, v, v-w, v, ..., v], notar que las aristas del grafo original no forman parte de este grafo.

IS => PS:
Teniendo en cuenta que el conjunto de caminos pedidos tiene V elementos y necesitamos k disjuntos, es muy parecido a Independent Set. Si tenemos un Independent Set de tamaño k en el grafo original, los caminos que recibe Path Selection son de ida y vuelta, por cada vértice tenemos un solo camino que lo integra y a su vez a todos los vértices arista que creamos que conectan con este vértice, por lo que esto garantiza que son caminos posibles pero a su vez contiene a los vértices arista que otros vértices originales también tienen en sus respectivos caminos sii son adyacentes en el grafo original. Si existen caminos disjuntos entonces van a diferir en estos vértices arista, estos vértices arista representan aristas en el grafo original, por lo que para que sean disjuntos 2 caminos los vértices responsables del ambos caminos no pueden ser adyacentes en el grafo original, pero nosotros ya sabemos que podemos conseguir k de ellos que no lo sean, entonces representando a los vértices como caminos podemos conseguir k disjuntos.

PS => IS:
Teniendo k caminos disjuntos podríamos obtener al representante de cada uno que es el único vértice dentro de cada camino que es original (que no es vértice arista). Como ya sabemos que tenemos k disjuntos, tenemos k vértices representantes que no aparecen en los caminos de los demás, pero, solo pueden ser disjuntos si no tienen vértices arista entre ellos, osea ser adyacentes, entonces tenemos k vértices independientes.
"""
