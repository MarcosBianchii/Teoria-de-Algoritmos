# (★) Explicar por qué el Algoritmo de Dijkstra (para obtener caminos mínimos desde un vértice, en un grafo con pesos positivos) es un Algoritmo Greedy.

"""
Un algoritmo Greedy es un algoritmo que busca de forma local el mejor resultado esperando que luego de varias iteraciones llegar a la solucion optima o una buena aproximacion del problema.

El algoritmo de Dijkstra es un algoritmo Greedy porque navega un grafo tomando siempre la arista conocida con menor peso. Esto lo logra utilizando un heap, se acerca a la solucion global donde durante varias iteraciones toma la mejor decision en el momento sin importar si mas tarde fuera o no la mejor decision.
"""
