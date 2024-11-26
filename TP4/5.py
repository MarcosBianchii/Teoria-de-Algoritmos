# Implementar un Autómata Finito No Determinista que acepte las cadenas que cumplan con la expresión regular: ((ab)+ba*)?(b*(ab)*)

# Notar que la expresión es equivalente a: ((ab)+ba*)?b*(ab)*

# Como recordatorio:

# El símbolo + indica que el símbolo anterior (o grupo, si está entre paréntesis) aparece al menos una vez (puede aparecer muchas veces, de forma contigua).

# El símbolo ? indica que el símbolo anterior (o grupo, si está entre paréntesis) puede aparecer una vez, o no estar (es decir, es opcional).

# El símbolo * indica que el símbolo anterior (o grupo, si está entre paréntesis) puede aparecer tantas veces como sea (puede ser ninguna o muchas) de forma contigua.

from automata import Automata


def expresion():
    a = Automata()
    a.estado("Q0", es_inicial=True, es_final=True)
    a.estado("Q1")
    a.estado("Q2", es_final=True)
    a.estado("Q3", es_final=True)
    a.estado("Q4", es_final=True)
    a.estado("Q5")
    a.estado("Q6", es_final=True)

    a.transicion_estado("Q0", "Q1", "a")
    a.transicion_estado("Q0", "Q4", "b")
    a.transicion_estado("Q1", "Q2", "b")
    a.transicion_estado("Q2", "Q1", "a")
    a.transicion_estado("Q2", "Q3", "b")
    a.transicion_estado("Q3", "Q3", "a")
    a.transicion_estado("Q3", "Q4", "b")
    a.transicion_estado("Q4", "Q5", "a")
    a.transicion_estado("Q4", "Q4", "b")
    a.transicion_estado("Q5", "Q6", "b")
    a.transicion_estado("Q6", "Q5", "a")
    return a
