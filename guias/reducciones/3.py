# (★★) Dados los problemas de decisiones de Independent Set y Vertex Cover, realizar dos reducciones.

"""
Teorema: S es un Independent Set de G sii V-S es Vertex Cover de G.
"""

# a. Reducir Independent Set a Vertex Cover.

"""
Teniendo un solucionador de Vertex Cover VC(g, k) podemos utilizarlo de la siguiente manera.

G tiene un Independent Set de tamaño k si VC(g, |V| - k), osea, existe un Vertex Cover de tamaño |V| - k. Por el teorema de arriba podemos concluir que existe un Vertex Cover de |V| - k sii existe un Independent Set de |V| - (|V| - k) = |V| - |V| + k = k.
"""

# b. Reducir Vertex Cover a Independent Set.

"""
Teniendo un solucionador de Independent Set IS(g, k) podemos utilizarlo de la siguiente manera.

G tiene un Vertex Cover de tamaño k si IS(g, |v| - k), es análogo a la situación contraria. Eexiste IS(g, |v| - k) sii existe VC(g, k).
"""
