# (★★) Definir los problemas de decisión de Independent Set y K-Clique. Hacer una reducción de Independet Set a K-Clique. Dada esta reducción, ¿podemos afirmar que K-Clique es un problema NP-Completo?

"""
Problema de decisión del Independent Set:
Dado un grafo y un número entero `k`, determinar si existe un subconjunto de vértices no adyacentes entre ellos de a lo sumo tamaño k.

Problema de decisión del K-Clique:
Dado un grafo y un número entero `k`, determinar si existe un subgrafo k-completo dentro del grafo original.

Para determinar que K-Clique es NP-Completo, hay que probar que está en NP y podemos por ejemplo intentar reducir Independent Set a K-Clique, si lo logramos entonces K-Clique es NP-Completo.
"""


def verificador_k_clique(grafo, k, clique):
    """
    La complejidad del verificador es O(V^2)
    """
    if len(clique) < k:
        return False

    # O(V)
    if any(v not in grafo for v in clique):
        return False

    # O(V^2)
    n = len(clique)
    for i in range(n):
        for j in range(i + 1, n):
            if (clique[i], clique[j]) not in grafo:
                return False

    return True


"""
Como la complejidad del verificador es polinómica, entonces K-Clique está en NP.

    def independent_set(grafo, k):
        # transformacion
        return k_clique(grafo_inverso, k)

Definimos el grafo inverso como el grafo donde todas las aristas que estaban en el original ahora no, y las que no estaban ahora sí. Este nuevo grafo tiene un k-clique sii existe un independent set en el grafo original.

K-Clique => Independent Set:
Si existe un K-Clique en un grafo, por definición hay un subgrafo k-comleto, es decir, existen k vértices tal que cada uno de ellos es adyacentes con los k-1 restantes (como mínimo). Tomando el complemento del grafo, ahora estos vértices no son adyacentes entre ellos, osea, existen k vértices independientes.

Independent Set => K-Clique:
Si existe un independent set de k vértices, entonces hay k vértices tal que ninguno de ellos es adyacente, osea, no existen aristas entre ellos. Tomando el grafo complemento los conectamos a todos ellos formando un k-clique.

Podemos afirmar que K-Clique es un problema NP-Completo.
"""
