# (★★) En su tiempo libre, Carlitos colecciona figuritas del mundial. Incluso a más de un año de la coronación de gloria, hay mucho entusiasmo por estas. Llegó a coleccionar tantas que ahora se dedica a revenderlas (para sacar unos pesos extra de su trabajo principal como publicista). Tiene tantas figuritas que ya no revende al público directamente, sino a otros revendedores y cadenas de kioscos. En general, cuando le piden, le pide un lote de figuritas “por una cantidad determinada de dinero”. Cada tipo de figurita tiene un valor diferente (es decir, la de Messi no vale lo mismo que la del Bobo Weghorst). Podemos decir que absolutamente todos los tipos de figuritas tienen valores diferentes, todos valores enteros, y que Carlitos cuenta con una cantidad ridículamente alta de cada una de ellas. Por un análisis que hizo, sabe que si le piden figuritas por un determinado monto, le conviene dar la menor cantidad de figuritas posibles (siempre cumpliendo con el monto exacto pedido), incluso repitiendo figuritas en caso de ser necesario. El problema de las figuritas de Carlitos dice: dados los valores de los diferentes tipos de figuritas y un monto al que llegar, determinar cuáles figuritas debe dar Carlitos para cumplir exactamente con dicho monto dando la mínima cantidad de figuritas para ello. Asumir todos valores enteros, y que hay figurita de valor 1. Por otro lado, recordemos que el Problema de SubsetSum es NP-Completo. Redefinir ambos problemas en sus versiones de problema de decisión, y realizar una reducción polinomial de uno a otro. ¿Podemos con esta reducción afirmar que el problema de Carlitos es NP-Completo?

"""
El problema de decisión de Carlitos es:
Dados los valores de distintas figuritas, un monto `w` al que llegar y un número entero `k`, determinar si existe alguna combinación de a lo sumo k valores de figuritas tales que sumados sea igual a w.

El problema de decisión de Subset Sum es:
Dado un arreglo de números y un número entero `w`, determinar si es posible mediante alguna combinación de los números en el arreglo obtener una suma de w.
"""


def validador_carlitos(figuritas, w, k, elegidas):
    """
    La complejidad del verificador es O(n)
    """
    # O(n)
    if any(f not in figuritas for f in elegidas):
        return False

    if len(elegidas) > k:
        return False

    # O(n)
    if sum(elegidas) != w:
        return False

    return True


"""
Como la complejidad del verificador es polinómica, el problema de Carlitos está en NP.

    def carlitos(figuritas, w, k):
        # transformacion
        return subset_sum(numeros, w)

Duplicamos k veces cada valor dentro del arreglo de numeros entrante. De esta forma garantizamos que podemos agarrar k veces cualquier figurita. Algo mejor es duplicarlas floor(w / f_i) veces.

Existen k valores de figuritas tales que su suma sea como mínimo w sii existe un Subset Sum de

Carlitos => SS:
Si existen k figuritas tales que tengan un valor sumado de w, Carlitos solo puede tener hasta k veces la misma figurita, pues la solución tiene k figuritas. Como repetimos k veces cada una, podemos garantizar que a lo sumo se tomó k veces alguna y de este modo existe un subconjunto que sume w dentro del arreglo modelo.

SS => Carlitos:
Si existen k números tales que tengan un valor sumado de w en el arreglo modelo, esto significa que si ningúno aparece más de k veces entonces Carlitos va a encontrar la solución al problema también, como la solución de Subset Sum tiene a lo sumo k números entonces Carlitos los valores particulares no van a poder aparecer más de k veces, puesto que toda la solución tiene k números.
"""
