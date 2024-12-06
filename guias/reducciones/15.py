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

Podríamos reducir el problema de Dominating Set a Submarinos si para cada vértice creamos un submarino tal que esté en rango de todos los submarinos de los que és vértice adyacente en el grafo. Hay un problema y es que como máximo un vértice puede tener un grado de 24, pues no entran en la matriz. Si pudieramos parametrizar el rango entonces sí podríamos reducir cualquier instancia del problema de dominating set a submarinos, por como está planteado el problema no es posible.

    def submarinos(matriz, k):
        # transformacion
        return dominating_set(grafo, k)

En este sentido, si es posible, por cada submarino vamos a crear un 25-Clique, estos representan los casilleros de los que este submarino puede ser iluminado. Si un casillero alcanza a dos submarinos en simultaneo entonces este vértice estará conectado con todos los vértices del otro clique también.

Entonces se pueden iluminar los submarinos con a lo sumo k faros sii existe un Dominating Set en el grafo modelo.

S => DS:
Si se pueden cubrir a todos los submarinos con a lo sumo k faros, entonces quiere decir que para todo submarino, este es cubierto por algún faro. En el grafo modelo, esto se representa como que dentro de cada 25-Clique, hay por lo menos un vértice dominante. Como hay misma la misma cantidad de submarinos como 25-Cliques en el grafo modelo y la posibilidad de iluminar a más de un submarino está tomada en cuenta, pues si fuera posible, este vértice dominaría a todos los cliques, entonces se dá Dominating Set con esa misma cantidad de faros.

DS => S:
Si existe un Dominating Set de a lo sumo k vértices, entonces esto quiere decir que para todo vértice, este es dominante o dominado por algún adyacente. Por como modelamos el grafo, cada 25-Clique tiene por lo menos a 1 vértice que domine al resto, como la posición de los submarino está incluida dentro del grafo como alguno de estos vértices, estos son dominados o dominan al resto. Como existen a lo sumo k vértices (siendo los faros) que dominan al resto (algunas son casilleros donde hay submarinos), entonces se dá Submarinos de a lo sumo k faros.
"""
