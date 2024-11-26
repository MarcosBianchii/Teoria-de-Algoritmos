class Automata:
    def __init__(self):
        self._qs = {}
        self._q = None
        self._final = set()

    def estado(self, nombre, es_inicial=False, es_final=False):
        if nombre in self._qs:
            raise ValueError("Este estado ya existe dentro del automata")

        self._qs[nombre] = {}
        if es_inicial:
            self._q = nombre
        if es_final:
            self._final.add(nombre)

    def transicion_estado(self, nombre1, nombre2, simbolo):
        if nombre1 not in self._qs or nombre2 not in self._qs:
            raise ValueError("Esta trancisión es inválida")

        self._qs[nombre1][simbolo] = nombre2

    def ejectuar(self, string):
        if self._q is None:
            raise ValueError("No hay ningún estado inicial")

        if len(self._final) < 0:
            raise ValueError("No hay ningún estado final")

        for x in string:
            if x not in self._qs[self._q]:
                return False

            self._q = self._qs[self._q][x]

        return self._q in self._final
