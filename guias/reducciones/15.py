# (★★) Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos. El problema es dar la cantidad mínima de faros que se necesitan para que todos los submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”). ¿Se encuentra este problema en NP? ¿Qué problema NP-Completo visto en la cursada es parecido al problema definido? Definir en ambos casos el problema de decisión. ¿qué reducción podríamos hacer? ¿Podemos concluir que este problema es un problema NP-Completo?

"""
El problema de decisión del problema de los submarinos es:
Dada una matriz con submarinos y un número entero `k`, determinar si es posible usando a lo sumo k faros iluminar a todos los submarinos.

El problema se parece a Dominating Set, su problema de decisión es:
Dado un grafo y un número entero `k`, deteminar si es posible obtener un subconjunto de vértices tal que todos los vértices del grafo o bien estén contenidos en él o sea adyacente a alguno que sí lo está.
"""


def verificador_submarinos(matriz, k, faros):
    """
    La complejidad del verificador es O(n * m + s * f)
    """
    if len(faros) > k:
        return False

    n = len(matriz)
    m = len(matriz[0])

    def cubre(faro, submarino):
        fx, fy = faro
        sx, sy = submarino
        rx, ry = fx - sx, fy - sy
        return max(abs(rx), abs(ry)) <= 2

    # O(n * m + s * f)
    for i in range(n):
        for j in range(m):
            if matriz[i][j] == 1:
                for faro in faros:
                    if not cubre(faro, (i, j)):
                        return False

    return True


"""
Como la complejidad del verificador es poliónomica, entonces el problema del submarino está en NP.

    def dominating_set(grafo, k):
        # transformacion
        return submarinos(matriz, k)

Podríamos reducir el problema de Dominating Set a Submarinos si para cada vértice creamos un submarino tal que esté en rango de todos los submarinos de los que és vértice adyacente en el grafo. Hay un problema y es que como máximo un vértice puede tener un grado de 24, pues no entran en la matriz. Si pudieramos parametrizar el rango entonces sí podríamos reducir toda instancia del problema de dominating set a submarinos, por como está planteado el problema no es posible.

    def submarinos(matriz, k):
        # transformacion
        return dominating_set(grafo, k)

En este sentido, si es posible, por cada submarino creamos un vértice en un grafo. Si 2 submarinos solapan su rango entonces creamos una arista entre sus vértices. n submarinos pueden ser cubiertos con a lo sumo k faros sii existe un dominating set de a lo sumo k vértices en el grafo modelo.

S => DS:
Si se pueden cubrir a todos los submarinos con a lo sumo k faros, entonces quiere decir que para todo submarino, este es cubierto unicamente por un faro o está dentro su rango junto a más submarinos. En el grafo modelado, esto se representa como, si un submarino es el único en un faro, entonces este está dentro del conjunto de dominación, si comparte faro con otros, tomamos algúno de ellos en el conjunto, estos vértices van a ser adyacentes porque por definición del grafo, son adyacentes si sus rangos solapan, o en otras palabras, podemos insertar un faro tal que ilumine a ambos.

DS => S:
Si existe un dominating set de a lo sumo k vértices, entonces esto quiere decir que para todo vértice este está en el conjunto de dominación o es adyacente a otro que lo és. En la matriz de submarinos, tendremos que si un vértice está dentro del conjunto y no tiene adyacentes, entonces este submarino puede tener un faro justo encima. Por otro lado si un vértice está dentro del conjunto con un grado mayor a 0, entonces el faro va en cualquiera de las posiciones intersecciones entre el rango de este vértice y sus adyacentes. Como son adyacentes sii existe esta intersección, entonces todo submarino puede ser cubierto.

"""
