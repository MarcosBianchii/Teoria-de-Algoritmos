# (★★) Tenemos una ruta recta muy larga, de K kilómetros, sobre la cual hay casas dispersas. En dichas casas vive gente que usa mucho sus celulares. El intendente a cargo la ruta debe renovar por completo el sistema de antenas, teniendo que construir sobre la ruta nuevas antenas. Cada antena tiene un rango de cobertura de R kilómetros(valor constante conocido). Implementar un algoritmo Greedy que reciba las ubicaciones de las casas, en número de kilómetro sobre esta ruta(números reales positivos) desordenadas, y devuelva los kilómetros sobre los que debemos construir las antenas para que todas las casas tengan cobertura, y se construya para esto la menor cantidad de antenas posibles. Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. ¿El algoritmo da la solución óptima siempre?

from math import inf


def cobertura(casas, R, K):
    """
    El algoritmo es optimo porque aprovecha al maximo la cobertura de las antenas, hay que
    cubrir todas las casas entonces poner las antenas lo mas a la derecha posible es la mejor
    opcion siempre.

    El algoritmo es Greedy porque itera las casas por altura, donde abastece a las casas con
    señal pensando en las casas que vienen a futuro. Al encontrar una casa sin señal, pone una
    nueva antena a R metros, por lo que alcanza a esta casa y tiene 2*R metros de antena por
    delante para otras casas que pueden o no caer dentro de la cobertura.

    La regla simple es: Si una casa no tiene cobertura entonces pongamos una antena que le de
    señal lo mas adelante posible para que tambien de señal a casas que todavia no vimos.

    La complejidad del algoritmo es O(nlogn)
    """
    # O(nlogn)
    casas.sort()

    # O(n)
    antenas = []
    cubierto = -inf
    for casa in casas:
        if cubierto < casa:
            antena = min(casa + R, K)
            antenas.append(antena)
            cubierto = antena + R

    return antenas
