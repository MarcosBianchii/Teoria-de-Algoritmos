# (★★) Decimos que dos caminos son disjuntos si no comparten aristas (pueden compartir nodos). Dado un grafo dirigido y dos vértices s y t, encontrar el máximo número de caminos disjuntos s-t en G. Dar una metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se consigue el máximo número de caminos disjuntos. ¿Cuál es el orden temporal de la solución implementada?

"""
Creamos un grafo residual que tenga todos los arcos del original con la salvedad de que todos sus pesos sean igual a 1, de esta forma representamos que un arco forma o no parte de algún camino ya tomado. Corremos ford-fulkerson y conseguimos los flujos de cada arco, el flujo máximo es igual a la cantidad de caminos y los caminos tomados pueden ser construidos a partir del diccionario de flujos, donde podemos arrancar desde s y tomar todos los arcos salientes con flujo 1 hasta llegar a t.
"""

from utils import encontrar_camino
from ..grafo import Grafo


def ford_fulkerson(red, s, t):
    flujos = {(v, w): 0 for v in red for w in red.adyacentes(v)}

    while (camino := encontrar_camino(red, s, t)) is not None:
        for i in range(1, len(camino)):
            v, w = camino[i - 1], camino[i]
            flujos[(v, w)] += 1
            red.borrar_arista(v, w)

    return flujos


def caminos_disjuntos(grafo: Grafo, s, t):
    red = Grafo(dirigido=True, vertices_init=grafo)

    for v in grafo:
        for w in grafo.adyacentes(v):
            red.agregar_arista(v, w, 1)

    flujos = ford_fulkerson(red, s, t)
    return sum(flujo for (_, w), flujo in flujos.items() if w == t)
