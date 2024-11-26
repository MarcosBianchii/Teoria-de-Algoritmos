class Automata:
    def __init__(self):
        self._qs = {}
        self._inicial = None
        self._final = set()

    def estado(self, nombre, es_inicial=False, es_final=False):
        if nombre in self._qs:
            raise ValueError("Este estado ya existe dentro del automata")

        self._qs[nombre] = {}
        if es_inicial:
            self._inicial = nombre
        if es_final:
            self._final.add(nombre)

    def transicion_estado(self, nombre1, nombre2, simbolo):
        if nombre1 not in self._qs or nombre2 not in self._qs:
            raise ValueError("Esta trancisión es inválida")

        self._qs[nombre1][simbolo] = nombre2

    def ejectuar(self, string):
        if self._inicial is None:
            raise ValueError("No hay ningún estado inicial")

        if len(self._final) < 0:
            raise ValueError("No hay ningún estado final")

        q = self._inicial
        for x in string:
            if x not in self._qs[q]:
                return False

            q = self._qs[q][x]

        return q in self._final
