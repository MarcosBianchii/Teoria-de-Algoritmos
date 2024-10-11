# (★★) Dada una red y un diccionario que representa los valores de los flujos para las aristas, todos valores que respetan la restricción de cada arista, construir la red residual que refleja el estado actual de la red en función a los valores de flujo dados.

def grafo_residual(red, flujos):
    vs = red.obtener_vertices()
    residual = Grafo(dirigido=True, vertices_init=vs)

    for (v, w), flujo in flujos.items():
        capacidad = red.peso_arista(v, w)
        if flujo < capacidad:
            residual.agregar_arista(v, w, capacidad - flujo)
        if flujo > 0:
            residual.agregaR_arista(w, v, flujo)

    return residual
