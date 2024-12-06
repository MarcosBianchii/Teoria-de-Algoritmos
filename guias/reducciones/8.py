# (★★) Definir los problemas de decisión de Camino Hamiltoniano y Ciclo Hamiltoniano. Sabiendo que Ciclo Hamiltoniano es NP-Completo, demostrar que Camino Hamiltoniano es NP-Completo.

"""
Problema de decisión del Camino Hamiltoniano:
Dado un grafo, determinar si existe un camino tal que pase una sola vez por cada vértice.

Problema de decisión del Ciclo Hamiltoniano:
Dado un grafo, determinar si existe un ciclo tal quepase una sola vez por cada vértice.
"""


def verificador_camino_hamiltoniano(grafo, camino):
    """
    La complejidad del verificador es O(V)
    """
    if len(camino) != len(grafo):
        return False

    # O(V)
    if any(v not in grafo for v in camino):
        return False

    # O(V)
    if len(camino) != len(set(camino)):
        return False

    # O(V)
    for i in range(1, len(camino)):
        if (camino[i - 1], camino[i]) not in grafo:
            return False

    return True


"""
Como la complejidad del verificador es polinómica, entonces Camino Hamiltoniano está en NP.

    def ciclo_hamiltoniano(grafo):
        # transformacion
        return camino_hamiltoniano(grafo)

Creamos un grafo dirigido a partir del original donde para cada arista creamos un par de arcos tal que uno vaya y el otro vuelva. Tomamos algún vértice aleatorio y lo "partimos" de forma que una de las partes se lleve consigo todos los arcos adyacentes y la otra los arcos incidentes.

Existe un ciclo hamiltoniano sii existe un camino hamiltoniano en el grafo nuevo.

Ciclo Hamiltoniano => Camino Hamiltoniano:
Es siempre verdadera, camino hamiltoniano es un caso particular de ciclo hamiltoniano.

Camino Hamiltoniano => Ciclo Hamiltoniano:
Si existe un camino hamiltoniano en el nuevo grafo, este obligatoriamente arranca y termina en los vértices de partición, pues, la única forma de llegar al vértice de adyacencias original es arrancando el cámino en él, esto es obligatorio, ya que hay que pasar por todos los vértices. La única forma de terminar de atravesar todos los vértices es terminando en el vértice de incidencias, pues, si llegaramos a él antes, no podríamos continuar con el camino.
"""
