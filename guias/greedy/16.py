# (★★★) El club de Amigos de Siempre prepara una cena en sus instalaciones en la que desea invitar a la máxima cantidad de sus n socios. Sin embargo por protocolo cada persona invitada debe cumplir un requisito: Sólo puede ser invitada si conoce a al menos otras 4 personas invitadas.

# a. Nos solicitan seleccionar el mayor número posible de invitados. Proponer una estrategia greedy óptima para resolver el problema.

class Grafo:
    pass


# conocidos: lista de pares de personas que se conocen, cada elemento es un (a, b)
def obtener_invitados(conocidos):
    grafo = Grafo()

    for v, w in conocidos:
        if v not in grafo:
            grafo.agregar_vertice(v)
        if w not in grafo:
            grafo.agregar_vertice(w)
        if not grafo.estan_unidos(v, w):
            grafo.agregar_arista(v, w)

    while len(grafo) > 0:
        quitar = [v for v in grafo if len(grafo.adyacentes(v)) < 4]
        if not quitar:
            break

        for v in quitar:
            grafo.borrar_vertice(v)

    return grafo.obtener_vertices()


# b. Los organizadores desean que cada invitado pueda conocer nuevas personas. Por lo que nos solicitan que adicionemos una nueva restricción a la invitación: Sólo puede asistir si NO conoce al menos otras 4 personas invitadas. Modifique su propuesta para satisfacer esta nueva solución.
