# (★) Explicar por qué el Algoritmo de Prim (para obtener el MST de un grafo no dirigido) es un Algoritmo Greedy.

"""
Un algoritmo Greedy es un algoritmo que busca de forma local el mejor resultado esperando que luego de varias iteraciones llegar a la solucion optima o una buena aproximacion del problema.

El algoritmo de Prim es un algoritmo Greedy porque de forma iterativa busca soluciones locales al problema que se acerquen a la solucion global. Comienza en un vertice del grafo, descubriendo sus aristas y vertices vecinos, se queda con la arista menos pesada y utilizando un heap y avanza con esto en mente, no formar ciclos y siempre tomar la arista mas barata conocida.
"""
