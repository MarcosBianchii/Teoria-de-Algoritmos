# (★) Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. El listado(ordenado por nombre del pueblo) contiene el número de kilómetro donde está ubicada cada una. Se desea ubicar la menor cantidad de patrullas policiales(en las bifurcaciones) de tal forma que no haya bifurcaciones con vigilancia a más de 50 km. Justificar que la solución es óptima. Indicar y justificar la complejidad del algoritmo implementado. Ejemplo:

# Ciudad	 Bifurcación
# Castelli	 185
# Gral Guido 242
# Lezama	 156
# Maipú	     270
# Sevigne	 194

# Si pongo un patrullero en la bifurcación de Lezama, cubro Castelli y Sevigne. Pero no Gral Guido y Maipú. Necesitaría en ese caso, poner otro. Agrego otro patrullero en Gral Guido. Con eso tengo 2 móviles policiales en bifurcaciones que cubren todas los accesos a todas las ciudades con distancia menor a 50km.

# En un caso alternativo donde solamente se consideren las bifurcaciones de Castelli, Gral Guido y Sevigne, la única solución óptima sería colocar un móvil policial en Sevigne.


from math import inf

def bifurcaciones_con_patrulla(ciudades):
    """
    La complejidad del algoritmo es O(nlogn)
    """
    if len(ciudades) == 0:
        return []

    # O(nlogn)
    ciudades.sort(key=lambda x: x[1])
    rango = ciudades[0][1] + 50
    patrulleros = []
    cubierto = -inf

    # O(n)
    for i in range(1, len(ciudades)):
        _, altura = ciudades[i]

        if rango < altura and cubierto < altura:
            anterior = ciudades[i - 1]
            patrulleros.append(anterior)
            cubierto = anterior[1] + 50
            if i + 1 < len(ciudades):
                rango = ciudades[i + 1][1] + 50

    altura = ciudades[-1][1]
    if cubierto < altura:
        patrulleros.append(ciudades[-1])

    return patrulleros

# 50        90  110            200   222    249     300
# |---------|----|--------------|-----|------|-------|


# Lezama	 156
# Castelli	 185
# Sevigne	 194
# Gral Guido 242
# Maipú	     270

# 156     185 194          242     270
#  |-------|---|------------|-------|