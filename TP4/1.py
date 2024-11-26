# Implementar un Autómata Finito Determinista que describa al Lenguaje que acepta todos las cadenas de 0 y 1s tales que dicho input represente en binario a una potencia de 2.

from automata import Automata


def automata_potencias_2():
    a = Automata()
    a.estado("Q0", es_inicial=True)
    a.estado("Q1", es_final=True)
    a.estado("Q2")

    a.transicion_estado("Q0", "Q0", "0")
    a.transicion_estado("Q0", "Q1", "1")
    a.transicion_estado("Q1", "Q1", "0")
    a.transicion_estado("Q1", "Q2", "1")
    a.transicion_estado("Q2", "Q2", "0")
    a.transicion_estado("Q2", "Q2", "1")
    return a
