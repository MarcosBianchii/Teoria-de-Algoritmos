# Implementacion de grafo con la misma interfaz que en RPL.

from copy import deepcopy


class Grafo:
    def __init__(self, dirigido=False, vertices_init=[]):
        self._vs = {v: {} for v in vertices_init}
        self._dir = dirigido

    def agregar_vertice(self, v):
        if v in self:
            raise KeyError(f"{v} ya existe en el grafo")

        self._vs[v] = {}

    def agregar_arista(self, v, w, peso=1):
        if v not in self:
            raise KeyError(f"{v} no existe en el grafo")

        if w not in self:
            raise KeyError(f"{w} no existe en el grafo")

        if w in self._vs[v]:
            raise KeyError("La arista a agregar ya existe")

        self._vs[v][w] = peso
        if not self._dir:
            self._vs[w][v] = peso

    def borrar_vertice(self, v):
        if v not in self:
            raise KeyError("El vertice a borrar no existe")

        for w in self.adyacentes(v):
            self.borrar_arista(v, w)

        del self._vs[v]

    def borrar_arista(self, v, w):
        if v not in self:
            raise KeyError(f"{v} no existe en el grafo")

        if w not in self:
            raise KeyError(f"{w} no existe en el grafo")

        if w not in self._vs[v]:
            raise KeyError(f"({v}, {w}) no existe en el grafo")

        del self._vs[v][w]
        if not self._dir:
            del self._vs[w][v]

    def peso_arista(self, v, w):
        if v not in self:
            raise KeyError(f"{v} no existe en el grafo")

        if w not in self:
            raise KeyError(f"{w} no existe en el grafo")

        if w not in self._vs[v]:
            raise KeyError(f"({v}, {w}) no existe en el grafo")

        return self._vs[v][w]

    def estan_unidos(self, v, w):
        if v not in self:
            raise KeyError(f"{v} no existe en el grafo")

        if w not in self:
            raise KeyError(f"{w} no existe en el grafo")

        return w in self._vs[v]

    def cambiar_peso(self, v, w, peso):
        if v not in self:
            raise KeyError(f"{v} no existe en el grafo")

        if w not in self:
            raise KeyError(f"{w} no existe en el grafo")

        self._vs[v][w] = peso
        if not self._dir:
            self._vs[w][v] = peso

    def adyacentes(self, v):
        if v not in self:
            raise KeyError("El vertice para buscar sus adyacentes no existe")

        return list(self._vs[v])

    def copy(self):
        return deepcopy(self)

    def obtener_vertices(self):
        return list(self)

    def __len__(self):
        return len(self._vs)

    def __contains__(self, v):
        return v in self._vs

    def __iter__(self):
        return iter(self._vs)


def dominating_set(grafo, valores):
    n = len(grafo)
    mem = [0] * (n + 1)
    vs = grafo.obtener_vertices()

    mem[1] = mem[2] = valores[vs[0]]

    for i in range(3, n + 1):
        mem[i] = min(mem[i - 1] + valores[vs[i - 1]],
                     mem[i - 2] + valores[vs[i - 2]])

    return construir_solucion(mem, vs, valores)


def construir_solucion(mem, vs, valores):
    i = len(vs)
    sol = []

    while i > 0:
        if mem[i] == mem[i - 1] + valores[vs[i - 1]]:
            sol.append(vs[i - 1])
            i -= 1
        else:
            sol.append(vs[i - 2])
            i -= 2

    sol.reverse()
    return sol


g = Grafo(dirigido=True, vertices_init=[0, 1, 2, 3, 4, 5])

for i in range(len(g) - 2):
    g.agregar_arista(i + 1, i)

valores = {0: 1, 1: 4, 2: 8, 3: 3, 4: 1, 5: 10}
print(dominating_set(g, valores))
