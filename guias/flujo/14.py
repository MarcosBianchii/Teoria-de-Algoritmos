# (★★★) Se está formando una nueva comisión de actividades culturales de un pueblo. Cada habitante es miembro de 0 o más clubes, y de exactamente 1 partido político. Cada grupo de interés debe nombrar a un representante ante la nueva comisión de actividades culturales, con las siguientes restricciones: cada partido político no puede tener más de n/2 simpatizantes en la comisión, cada persona puede representar a solo un club, cada club debe estar representado por un miembro. Implementar un algoritmo que dada la información de los habitantes (a qué clubes son miembros, a qué partido pertenecen), nos dé una lista de representantes válidos. Indicar y justificar la complejidad del algoritmo implementado.

"""
Modelamos un grafo donde existen 4 capas donde tenemos algo así como:

fuente -> habitantes1 -> clubes -> sumidero
fuente -> habitantes2 -> partidos -> sumidero

El flujo de la red declara a los representantes de cada ente. Como todas las capacidades son 1, cada habitante puede solo ser representante de un club y un partido politico, mientras que cada ente puede ser representado por un solo habitante.

Las conecciones entre fuente se conecta a todos los habitantes, los habitantes se conectan al partido político al que forman parte y a los clubes de los que son miembros, luego cada ente se conecta al sumidero.

Esto también se puede partir en dos redes, una que decida los representantes de cada ente.
"""

from ..grafo import Grafo
from utils import encontrar_camino


def representantes(clubes, partidos):
    """
    Ambos parametros son diccionarios donde contienen a todos los habitantes como clave y a que club/partido pertenecen.

    La complejidad del algoritmo es O(h * c^2)
    """
    def crear_grafo(ente: dict):
        red = Grafo(dirigido=True, vertices_init=["fuente", "sumidero"])

        # O(h)
        for habitante, conecciones in ente.items():
            red.agregar_vertice(habitante)
            red.agregar_arista("fuente", habitante)

            # O(c) para clubes
            # O(1) para partidos
            for e in conecciones:
                if e not in red:
                    red.agregar_vertice(e)

                red.agregar_arista(habitante, e)
                if not red.estan_unidos(e, "sumidero"):
                    red.agregar_arista(e, "sumidero")

        return red

    def ford_fulkerson(red: Grafo):
        flujos = {(v, w): 0 for v in red for w in red.adyacentes(v)}

        while (camino := encontrar_camino("fuente", "sumidero")) is not None:
            for i in range(1, len(camino)):
                v = camino[i - 1]
                w = camino[i]

                # Por como armamos la red, sabemos
                # que siempre la capacidad minima es 1.
                flujos[(v, w)] += 1
                red.borrar_arista(v, w)

        return flujos

    def obtener_representantes(red: Grafo, flujos):
        representantes = {}

        # O(e)
        for (v, w), flujo in flujos:
            if flujo == 0:
                continue

            if v != "fuente" or w != "sumidero":
                representantes[w] = v

        return representantes

    red_clubes = crear_grafo(clubes)
    red_partidos = crear_grafo(partidos)

    flujos_clubes = ford_fulkerson(red_clubes)
    flujos_partidos = ford_fulkerson(red_partidos)

    repr_clubes = obtener_representantes(red_clubes, flujos_clubes)
    repr_partidos = obtener_representantes(red_partidos, flujos_partidos)

    return repr_clubes, repr_partidos
