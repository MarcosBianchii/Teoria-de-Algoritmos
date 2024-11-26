# Implementar un Autómata Finito No Determinista que acepte las cadenas que cumplan con la expresión regular: (aab)*(a, aba)*

# Como recordatorio:

# El símbolo * indica que el símbolo anterior (o grupo, si está entre paréntesis) puede aparecer tantas veces como sea (puede ser ninguna o muchas) de forma contigua.

# Esta expresión acepta todas las cadenas que tengan una cantidad indefinida de aab como inicio, luego puedan tener una cantidad indefinida de a o aba (que pueden estar intercaladas).

from automata import Automata


def expresion():
    a = Automata()
    a.estado("Q0", es_inicial=True, es_final=True)
    a.estado("Q1", es_final=True)
    a.estado("Q2", es_final=True)
    a.estado("Q3", es_final=True)
    a.estado("Q4")
    a.estado("Q5", es_final=True)
    a.estado("Q6", es_final=True)

    a.transicion_estado("Q0", "Q1", "a")
    a.transicion_estado("Q1", "Q2", "a")
    a.transicion_estado("Q1", "Q4", "b")
    a.transicion_estado("Q2", "Q5", "a")
    a.transicion_estado("Q2", "Q3", "b")
    a.transicion_estado("Q3", "Q1", "a")
    a.transicion_estado("Q4", "Q5", "a")
    a.transicion_estado("Q5", "Q6", "a")
    a.transicion_estado("Q6", "Q6", "a")
    a.transicion_estado("Q6", "Q4", "b")
    return a
