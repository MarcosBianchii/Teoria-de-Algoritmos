# Implementacion de grafo con la misma interfaz que en RPL.

class Grafo:
    def __init__(self, dirigido=False, vertices_init=[]):
        self._vs = {v: {} for v in vertices_init}
        self._dir = dirigido

    def agregar_vertice(self, v):
        if v in self:
            raise KeyError(f"{v} ya existe en el grafo")

        self._vs[v] = {}

    def agregar_arista(self, v, w, weight=1):
        if v not in self:
            raise KeyError(f"{v} no existe en el grafo")

        if w not in self:
            raise KeyError(f"{w} no existe en el grafo")

        if w in self._vs[v]:
            raise KeyError("La arista a agregar ya existe")

        self._vs[v][w] = weight
        if not self._dir:
            self._vs[w][v] = weight

    def borrar_vertice(self, v):
        if v not in self:
            raise KeyError("El vertice a borrar no existe")

        for w in self.adyacents(v):
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

        if w in self._vs[v]:
            raise KeyError(f"({v}, {w}) no existe en el grafo")

        return self._vs[v][w]

    def adyacentes(self, v):
        if v not in self:
            raise KeyError("El vertice para buscar sus adyacentes no existe")

        return list(self._vs[v])

    def vertices(self):
        return list(self)

    def __len__(self):
        return len(self._vs)

    def __contains__(self, v):
        return v in self._vs

    def __iter__(self):
        return iter(self._vs)
