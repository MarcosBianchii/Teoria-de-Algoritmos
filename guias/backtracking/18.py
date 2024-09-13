# (★★★) Implementar un algoritmo que, por backtracking, obtenga la cantidad total de posibles ordenamientos topológicos de un grafo dirigido y acíclico.

from grafo import Grafo


def contar_ordenamientos(grafo):
    indegs = {v: 0 for v in grafo}
    for v in grafo:
        for w in grafo.adyacentes(v):
            indegs[w] += 1

    def count_topo_sort(grado0):
        if not grado0:
            return 1

        cantidad = 0
        for v in grado0.copy():
            grado0.remove(v)
            for w in grafo.adyacentes(v):
                indegs[w] -= 1
                if indegs[w] == 0:
                    grado0.add(w)

            cantidad += count_topo_sort(grado0)

            grado0.add(v)
            for w in grafo.adyacentes(v):
                indegs[w] += 1
                if indegs[w] == 1:
                    grado0.remove(w)

        return cantidad

    grado0 = set(v for v, d in indegs.items() if d == 0)
    return count_topo_sort(grado0)


if __name__ == "__main__":
    grafo = Grafo(True, ["A", "B", "C", "D"])
    grafo.agregar_arista("A", "C")
    grafo.agregar_arista("B", "C")
    grafo.agregar_arista("B", "D")
    print(contar_ordenamientos(grafo))
