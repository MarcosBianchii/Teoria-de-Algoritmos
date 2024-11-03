# (★★★) Para ayudar a personas con problemas visuales (por ejemplo, daltonismo) el gobierno de Agrabah decidió que en una misma parada de colectivo nunca pararán dos colectivos que usen el mismo color. El problema es que ya saben que eso está sucediendo hoy en día, así que van a repintar todas las líneas de colectivos. Por problemas presupuestarios, desean pintar los colectivos con la menor cantidad posible k colores diferentes. Como no quieren parecer un grupo de improvisados que malgasta los fondos públicos, quieren hacer un análisis para saber cuál es ese mínimo valor para cumplir con lo pedido (pintar cada línea con alguno de los k colores, de tal forma que no hayan dos de mismo color coincidiendo en la misma parada). Considerando que se tiene la información de todas las paradas de colectivo y qué líneas paran allí, modelar el problema utilizando grafos e implementar un algoritmo que determine el mínimo valor k para resolver el problema. Indicar la complejidad del algoritmo implementado.

from ..grafo import Grafo


def pintar_colectivos(colectivos, paradas):
    grafo = Grafo(vertices_init=colectivos)

    for parada in paradas:
        for i in range(len(parada)):
            for j in range(i + 1, len(parada)):
                v = parada[i]
                w = parada[j]
                if not grafo.estan_unidos(v, w):
                    grafo.agregar_arista(v, w)

    vertices = grafo.obtener_vertices()
    colores = {}

    def validar_coloreo(v):
        for w in grafo.adyacentes(v):
            if w in colores and colores[v] == colores[w]:
                return False

        return True

    def es_k_coloreable(k, i):
        if i == len(grafo):
            return True

        v = vertices[i]
        for color in range(k):
            colores[v] = color

            if validar_coloreo(v):
                if es_k_coloreable(k, i + 1):
                    return True

        del colores[v]
        return False

    for i in range(1, len(grafo)):
        if es_k_coloreable(i, 0):
            return i

    return len(grafo)
