# (★★★) Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse. Implementar un algoritmo que, por backtracking, obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa(o en otras palabras, que dejan la menor cantidad de espacios vacíos).

def max_grupos_bodegon(P, W):
    max_gente = 0
    grupos = []

    def llenar_mesa(i, mesa, gente):
        nonlocal max_gente, grupos
        if gente > W:
            return False

        # Encontre una mejor solucion
        # a la que ya tenia
        if max_gente < gente:
            grupos = mesa.copy()
            max_gente = gente

        # Ya encontre la mejor solucion
        if max_gente == W:
            return True

        if i == len(P):
            return False

        grupo = P[i]
        mesa.append(grupo)
        if llenar_mesa(i + 1, mesa, gente + grupo):
            return True

        mesa.pop()
        if llenar_mesa(i + 1, mesa, gente):
            return True

        return False

    llenar_mesa(0, [], 0)
    return grupos
