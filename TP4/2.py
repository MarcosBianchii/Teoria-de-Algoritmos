# Implementar un Autómata Finito Determinista que describa al Lenguaje que acepta todos las cadenas de 0 y 1s tales que tienen una cantidad par tanto de 0s como de 1s.

from automata import Automata


def automata_pares_1y0():
    a = Automata()
    a.estado("Q0", es_inicial=True, es_final=True)
    a.estado("Q1")
    a.estado("Q2")
    a.estado("Q3")

    a.transicion_estado("Q0", "Q1", "0")
    a.transicion_estado("Q0", "Q2", "1")
    a.transicion_estado("Q1", "Q0", "0")
    a.transicion_estado("Q1", "Q3", "1")
    a.transicion_estado("Q2", "Q0", "1")
    a.transicion_estado("Q2", "Q3", "0")
    a.transicion_estado("Q3", "Q1", "1")
    a.transicion_estado("Q3", "Q2", "0")
    return a
