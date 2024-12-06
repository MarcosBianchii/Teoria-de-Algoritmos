# (★★) El Hitting-Set Problem se define de la siguiente forma: Dado un conjunto de elemento A de n elementos, m subconjuntos B_1, B_2, ..., B_m de A (B_i ⊆ A ∀i), y un número k, ¿existe un subconjunto C ⊆ A con |C| ≤ k tal que C tenga al menos un elemento de cada B_i (es decir, C ∩ B_i ≠ ∅)?

# Demostrar que el Hitting-Set Problem es un problema NP-Completo.

"""
Problema de decisión del Hitting-Set Problem:
Dado un conjunto de n elementos A, m subconjuntos de A B_i, y un número entero `k`, determinar si existe un subconjunto C incluído en A de por lo menos k elementos tal que C contenga al menos 1 elemento de cada B_i.

Propongo el problema NP-Completo Vertex Cover, su problema de decisión es:
Dado un grafo y un número entero `k`, determinar si existe un subconjunto de por lo menos k vértices tales que para toda arista del grafo, alguno de sus extremos sea parte del subconjunto.
"""


def verificador_hitting_set(A, Bs, k, C):
    """
    La complejidad del verificador es O(n * m)
    """
    if len(C) > k:
        return False

    # O(c)
    if any(c not in A for c in C):
        return False

    # O(n * m)
    for b in Bs:
        if all(x not in C for x in b):
            return False

    return True


"""
Como la complejidad del verificador es polinómica, Hitting-Set está en NP.

    def vertex_cover(grafo, k):
        # transformacion
        return hitting_set(V, E, k)

El conjunto de vértices pasa a ser A, B es un conjunto de conjuntos de pares de vértices, donde cada B_i se ve como {v, w} y tal existe sii la arista (v, w) existe en el grafo original. El valor de k es el mismo.

Existe un Vertex Cover de tamaño por lo menos k sii existe un Hitting Set de por lo menos tamaño k en el modelo.

VC => HS:
Si existe un Vertex Cover de tamaño k, eso significa que para cada arista uno de sus extremos se encuentra en el subconjunto C. Como pasa esto, necesariamente todos los B_i tienen por lo menos alguno de sus elementos en C, pues son las aristas, y de esta forma se da un HS de tamaño k.

HS => VC:
Si en nuestro modelo se da un HS de tamaño k, esto significa que C tiene k elementos tal que cada uno de ellos pertenece a por lo menos un B_i y todos ellos tienen alguno de sus elementos en C. Como los elementos de C son vértices y los elementos de B_i sus aristas, si tenemos por lo menos uno en cada B_i, esto significa que para toda arista del grafo, C contiene alguno de sus extremos. Por lo que se da un VC de tamaño k.
"""
