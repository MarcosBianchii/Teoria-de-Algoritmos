# (★★) Hacer un seguimiento de obtener el flujo máximo en la siguiente red de transporte, realizando las modificaciones previas que fueran necesarias. Luego, definir cuáles son los dos conjuntos del corte mínimo en dicha red.

def obtener_flujo():
    """
    El grafo original tiene dos sumideros y una arista antiparalela, se reestructura con
    un super_sumidero al que le entran de T y X. Se introduce un nuevo vertice que parte
    Z->W tal que Z->Y y Y->W con la misma capacidad.
    """
    flujo = {}
    flujo[("S", "V")] = 4
    flujo[("V", "T")] = 3
    flujo[("V", "W")] = 1
    flujo[("S", "W")] = 3
    flujo[("W", "T")] = 5
    flujo[("S", "U")] = 3
    flujo[("U", "W")] = 1
    flujo[("U", "Z")] = 2
    flujo[("Z", "X")] = 0
    flujo[("Z", "W")] = 0
    flujo[("W", "Z")] = 0
    flujo[("Z", "T")] = 2
    flujo[("T", "super_sumidero")] = 10
    flujo[("X", "super_sumidero")] = 0

    conjunto_fuente = ["S", "U", "V"]
    conjunto_super_sumidero = ["T", "W", "X", "Z", "super_sumidero"]

    return flujo, conjunto_fuente, conjunto_super_sumidero
