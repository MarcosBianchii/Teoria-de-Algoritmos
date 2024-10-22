# (★) El problema del Vertex Cover se define como: dado un grafo no dirigido, obtener el mínimo subconjunto de vértices del grafo tal que toda arista del grafo tenga al menos uno de sus vértices perteneciendo al subconjunto. Dicho conjunto es un Vertex Cover. Definir el problema de decisión del Vertex Cover. Luego, implementar un verificador polinomial para este problema. ¿Cuál es la complejidad del verificador implementado? Justificar

"""
El problema de decisión del Vertex Cover se define como:
Dado un grafo no dirigido y un valor entero `k`, evaluar si es posible obtener por lo menos un subconjunto de `k` vértices tal que todas las aristas del grafo tengan por lo menos alguno de sus vértices extremos dentro del subconjunto.
"""


def verificador_vertex_cover(grafo, k, vcover):
    """
    La complejidad del verificador es O(V + E)
    """
    if len(vcover) != k:
        return False

    # O(V)
    if any(v not in grafo for v in vcover):
        return False

    # O(V + E)
    for v in grafo:
        for w in grafo.adyacentes(v):
            if v not in vcover and w not in vcover:
                return False

    # O(V)
    conteo = {}
    for v in vcover:
        conteo[v] = conteo.get(v, 0) + 1
        if conteo[v] > 1:
            return False

    return True
