# (★★) Trabajamos para el mafioso Arnook, que es quien tiene la máxima influencia y poder en la zona costera de Ciudad República. Allí reina el caos y la delincuencia, a tal punto que quien termina organizando las pequeñas mafias locales no es otro sino Arnook. En particular, nos vamos a centrar en unos pedidos que recibe de parte de dichos grupos por el control de diferentes kilómetros de la ruta costera. Cada pequeña mafia le pide a Arnook control sobre un rango de kilómetros(por ejemplo, la mafia nro 1 le pide del kilómetro 1 al 3.5, la mafia 2 le pide del 3.3333 al 8, etc. . .). Si hay una mafia tomando control de algún determinado kilómetro, no puede haber otra haciendo lo mismo(es decir, no pueden solaparse). Cada mafia pide por un rango específico. Arnook no cobra por kilómetraje sino por “otorgar el permiso”, indistintamente de los kilómetros pedidos. Ahora bien, esto es una mafia, no una ONG, y no debe rendir cuentas con nadie, así que lo único que es de interés es maximizar la cantidad de permisos otorgados(asegurándose de no otorgarle algún lugar a dos mafias diferentes). Implementar un algoritmo Greedy que reciba los rangos de kilómetros pedidos por cada mafia, y determine a cuáles se les otorgará control, de forma que no hayan dos mafias ocupando mismo territorio, y a su vez maximizando la cantidad de pedidos otorgados. Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué el algoritmo planteado es Greedy. ¿El algoritmo da la solución óptima siempre?

# pedidos: lista de tuplas con (km inicio, km fin)
def asignar_mafias(pedidos):
    """
    El algoritmo es Greedy porque de forma iterativa otorga los kilometrajes teniendo en cuenta
    su altura maxima y que no se solape su altura minima con el anterior territorio. Es el mismo
    problema que el de scheduling de charlas donde queremos dar la maxima cantidad de charlas en
    un dia.

    Este algoritmo da la solucion optima siempre. Esto es porque ordenando los kilometrajes por
    su altura maxima, nosotros vamos a iterar hasta encontrar el proximo que mejor se acomode a
    la distribucion de territorios que ya teniamos y aseguramos que ninguno proximo vaya a terminar
    antes que el que estamos viendo en el momento (puesto que es el criterio de ordenamiento).

    La complejidad del algoritmo es O(nlogn)
    """
    def se_solapan(p0, p1):
        return p1[0] <= p0[1]

    if len(pedidos) == 0:
        return []

    # O(nlogn)
    pedidos.sort(key=lambda p: p[1])

    mafias = [pedidos[0]]
    # O(n)
    for i in range(1, len(pedidos)):
        pedido = pedidos[i]
        if not se_solapan(mafias[-1], pedido):
            mafias.append(pedido)

    return mafias
