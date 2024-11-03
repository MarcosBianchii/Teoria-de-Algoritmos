# (★★) Dado un grafo no dirigido BIPARTITO, un match es un subconjunto de las aristas en el cual para todo vértice v a lo sumo una arista del match incide en v (en el match, tienen grado a lo sumo 1). Decimos que el vértice v está matcheado si hay alguna arista que incida en él (sino, está unmatcheado). El matching máximo es aquel en el que tenemos la mayor cantidad de aristas (matcheamos la mayor cantidad posible). Dar una metodología para encontrar el matching máximo de un grafo, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se consigue el matching máximo. ¿Cuál es el orden temporal de la solución implementada?

"""
Primero tomamos una partición bipartita del grafo en dos conjuntos, creando arcos dirigidos de V1 a V2 con peso 1 sii existe la arista en el grafo original. Luego conectamos un nuevo vértice fuente a todos los vértices de V1 con peso 1. Para los vértices de V2 los conectamos a un vértice sumidero también con arcos de peso 1.

De esta forma modelamos el problema a una red de flujo, corremos ford-fulkerson y de esta forma va a devolver un matcheo representado por los flujos, siendo que la i-ésima arista es parte del matching sii tiene un flujo igual a 1. Por como modelamos el problema un vértice cualquiera puede solamente estar matcheado con un vértice (esto se representa por la capacidad 1 en el arco de salida al sumidero y entrada desde la fuente).

Conseguir la partición se logra en tiempo lineal usando un BFS por ejemplo, osea su complejidad es de O(V + E). La creación del grafo residual también, pues es insertar todos los vértices y un arco por arista del grafo original más una fuente y sumidero tal que la suma de sus grados sea igual a la cantidad de vértices. Correr ford-fulkerson es O(VE^2) pero esta vez por la topología del grafo podemos garantizar que su complejidad es O(V*E), pues al partir el conjunto de vértices en 2 la cantidad de matcheos es igual a la mínima cardinalidad entre estos 2 conjuntos que podemos acotar por V/2, entonces el algoritmo pasa de ser O(V * E^2) a O(V * E).

Por lo que la complejidad de la solución es O(V * E).
"""

from utils import encontrar_camino
from ..grafo import Grafo
from collections import deque


def partir_vertices(grafo: Grafo):
    colores = {}

    def bfs(v):
        q = deque([v])

        while q:
            v = q.popleft()
            for w in grafo.adyacentes(v):
                if w not in colores:
                    colores[w] = 1 - colores[v]
                    q.append(w)
                elif colores[w] == colores[v]:
                    raise ValueError("El grafo no es bipartito")

        for v in grafo:
            if v not in colores:
                colores[v] = 0
                bfs(v)

    v1 = set()
    v2 = set()
    for v, color in colores:
        if color == 0:
            v1.add(v)
        else:
            v2.add(v)

    return v1, v2


def ford_fulkerson(red, s, t):
    flujos = {(v, w): 0 for v in red for w in red.adyacentes(v)}

    while (camino := encontrar_camino(red, s, t)) is not None:
        for i in range(1, len(camino)):
            v, w = camino[i - 1], camino[i]
            flujos[(v, w)] += 1
            red.borrar_arista(v, w)

    return flujos


def particion_bipartita(grafo: Grafo):
    v1, v2 = partir_vertices(grafo)

    red = Grafo(dirigido=True, vertices_init=v1 + v2)
    red.agregar_vertice("fuente")
    red.agregar_vertice("sumidero")

    for v in v1:
        red.agregar_arista("fuente", v)
        for w in grafo.adyacentes(v):
            red.agregar_arista(w)

    for v in v2:
        red.agregar_arista(v, "sumidero")

    flujos = ford_fulkerson(red, "fuente", "sumidero")
    return set(arista for arista, flujo in flujos.items() if flujo == 1)
