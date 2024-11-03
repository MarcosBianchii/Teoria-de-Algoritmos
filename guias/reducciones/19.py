# (★★★) Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice de G: o bien (i) pertenece a D; o bien (ii) es adyacente a un vértice en D. El problema de decisión del set dominante implica, dado un grafo G y un número k, determinar si existe un set dominante D de a lo sumo tamaño k. Demostrar que el Dominating Set Problem es un problema NP-Completo. Ayuda: recomendamos recordar Vertex Cover, que puede ser útil para esto.

"""
Problema de decisión de Dominating Set:
Dado un grafo y un número entero `k`, determinar si es posible obtener un subconjunto de vértices tales que o todos los vértices del grafo estén en él, o sea adyacente a uno que sí lo está, siendo el conjunto de un tamaño de por lo menos k.

Problema de decisión de Vertex Cover:
Dado un grafo y un número entero `k`, determinar si es posible obtener un subconjunto de vértices tales que para toda arista en el grafo, por lo menos uno de sus extremos esté en el conjunto, siendo el conjunto de un tamaño de de por lo menos k.
"""


def verificador_dominating_set(grafo, k, dset):
    """
    La complejidad el verificador es O(v + e)
    """
    if len(dset) > k:
        return False

    # O(d)
    if any(v not in grafo for v in dset):
        return False

    # O(v + e)
    for v in grafo:
        for w in grafo.adyacentes(v):
            if v not in dset or w not in dset:
                return False

    return True


"""
Como la complejidad del verificador es polinómica, Dominating Set está en NP.

    def vertex_cover(grafo, k):
        # transformacion
        return dominating_set(grafo, k)

Tomamos el grafo original y por cada arista, creamos un nuevo vértice y conectamos desde cada extremo de la arista original otra arista al nuevo vértice. Creando triangulos por cada arista.

VC => DS:
Si existe un vertex cover de como mínimo k vértices en el grafo original, entonces tiene que existir un dominating set de por lo menos k vértices en el grafo modelo. Por como modelamos el grafo, si un vértice forma parte del vertex cover, entonces sabemos que ninguno de los vértices que agregamos pertenecen al conjunto de cubrimiento pero sí alguno de los otros dos, los originales, como tener alguno de ellos domina a los otros 2, entonces podemos estar seguro que agregando vértices y aristas de esta manera termina resultando en que dominamos a todos los vértices del grafo con la misma cantidad de vértices.

DS => VC:
Si existe un dominating set de como mínimo k vértices en el grafo modelo, entonces tiene que existir un vertex cover de por lo menos k vértices en el grafo original. El grafo modelo está compuesto por triangulos donde por cada triangulo hay 2 vértices originales y uno agregado, si los originales forman parte del conjunto de dominación, entonces forman parte del vertex cover, si el vértice agregado forma parte del conjunto de dominación, entonces tomamos alguno de los originales y lo insertamos en el conjunto de cubrimiento, de esta forma garantizamos que ambos conjuntos sean del mismo tamaño y se cumple que para todos los triangulos (osea todas las aristas del grafo original) alguno de sus extremos la cubra.
"""
