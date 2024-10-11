# (★★) Hacer un seguimiento de obtener el flujo máximo en la siguiente red de transporte, realizando las modificaciones previas que fueran necesarias. Luego, definir cuáles son los dos conjuntos del corte mínimo en dicha red.

def obtener_flujo():
    """
    El grafo original tiene dos fuentes y una arista antiparalela, se reestructura con
    una super_fuente que sale a S y X. Se introduce un nuevo vertice que parte Z->U tal
    que Z->Y y Y->U con la misma capacidad.
    """
    flujo = {}
    flujo[("super_fuente", "S")] = 7
    flujo[("super_fuente", "X")] = 2
    flujo[("S", "V")] = 4
    flujo[("S", "U")] = 3
    flujo[("V", "T")] = 3
    flujo[("V", "W")] = 1
    flujo[("W", "T")] = 6
    flujo[("U", "W")] = 4
    flujo[("X", "Z")] = 2
    flujo[("Z", "W")] = 1
    flujo[("Z", "U")] = 1
    flujo[("U", "Z")] = 0

    conjunto_super_fuente = ["super_fuente", "S", "U", "V", "W", "X", "Z"]
    conjunto_sumidero = ["T"]

    return flujo, conjunto_super_fuente, conjunto_sumidero
