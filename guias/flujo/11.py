# (★★★) Supongamos que tenemos un sistema de una facultad en el que cada alumno puede pedir hasta 10 libros de la biblioteca. La biblioteca tiene 3 copias de cada libro. Cada alumno desea pedir libros diferentes. Implementar un algoritmo que nos permita obtener la forma de asignar libros a alumnos de tal forma que la cantidad de préstamos sea máxima. Dar la metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se consigue la máxima cantidad de prestamos. ¿Cuál es el orden temporal de la solución implementada?

from utils import encontrar_camino, peso_minimo, actualizar_grafo_residual
from ..grafo import Grafo


def ford_fulkerson(red, s, t):
    flujos = {(v, w): 0 for v in red for w in red.adyacentes(v)}
    residual = red.copy()

    while (camino := encontrar_camino(residual, s, t)) is not None:
        min_cap = peso_minimo(camino)

        for i in range(1, len(camino)):
            v, w = camino[i - 1], camino[i]

            if red.estan_unidos(v, w):
                flujos[(v, w)] += min_cap
            else:
                flujos[(v, w)] -= min_cap

            actualizar_grafo_residual(residual, v, w, min_cap)

    return flujos


def libros(libros, alumnos):
    residual = Grafo(dirigido=True, vertices_init=libros + alumnos)
    residual.agregar_vertice("s")
    residual.agregar_vertice("t")

    # O(L * A)
    for libro in libros:
        residual.agregar_arista("s", libro, 3)

        for alumno in alumnos:
            residual.agregar_arista(libro, alumno)

    # O(A)
    for alumno in alumnos:
        residual.agregar_arista(alumno, "t", 10)

    # O(V * E)
    flujos = ford_fulkerson(residual, "s", "t")
    return sum(flujos[w] for w in residual.adyacentes("s"))


"""
1. Crear la red residual donde tenemos libros y alumnos.
2. Conectar cada libro con el sumidero con capacidad 3, entonces cada libro puede estar en a lo sumo 3 caminos.
3. Conectar todos los libros con todos los alumnos con capacidad 1 (se supone que un alumno no va a pedir el mismo libro mas de una vez).
4. Conectar todos los alumnos con el sumidero con capacidad 10, entonces cada alumno puede estar en a lo sumo 10 caminos.
5. Correr ford-fulkerson y devolver el flujo maximo.
"""
