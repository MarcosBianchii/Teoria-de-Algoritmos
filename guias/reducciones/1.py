# (★) El problema del Independent Set se define como: dado un grafo no dirigido, obtener el máximo subconjunto de vértices del grafo tal que ningun par de vértices del subconjunto sea adyacente entre si. Dicho conjunto es un Independet Set. Definir el problema de decisión del Independent Set. Luego, implementar un verificador polinomial para este problema. ¿Cuál es la complejidad del verificador implementado? Justificar

"""
El problema de decisión del Independent Set es:
Dado un grafo no dirigido y un valor entero `k`, evaluar si es posible obtener un subconjunto S de a lo sumo `k` vértices tal que ningún vértice dentro del subconjunto sea adyacente a otro dentro de S.
"""


def verificador_independent_set(grafo, k, iset):
    """
    La complejidad del verificador es O(V + E)
    """
    if len(iset) < k:
        return False

    # O(V)
    if any(v not in grafo for v in iset):
        return False

    # O(S + E)
    for v in iset:
        for w in grafo.adyacentes(v):
            if w in iset:
                return False

    return True
