# (★★) Definir los problemas de decisión de Subset Sum y Problema de la Mochila. Sabiendo que Subset Sum es NP-Completo, demostrar que el Problema de la Mochila es NP-Completo.

"""
Problema de decisión de Subset Sum:
Dada una colección de números y un número entero `k`, determinar si existe un subconjunto de números tal que su suma sea exactamente k.

Problema de decisión de la Mochila:
Dada una colección de valores, pesos asociados, un valor a alcanzar `v` y un peso máximo `w`, determinar si existe un subconjunto de elementos donde la suma de sus valores es mayor o igual a v y la suma de sus pesos es menor o igual a w.
"""


def verificador_mochila(elementos, v, w, mochila):
    """
    La complejidad del verificador es O(n)
    """
    # O(n)
    if sum(x[0] for x in mochila) > w:
        return False

    # O(n)
    if sum(x[1] for x in mochila) < v:
        return False

    # O(n)
    elementos = set(elementos)
    if any(x not in elementos for x in mochila):
        return False

    return True


"""
Como la complejidad del verificador es polinómica, entonces el problema de la mochila está en NP.

    def subset_sum(coleccion, k):
        # transformacion
        return mochila(elementos, k, k)

Sabiendo que Subset Sum es NP-Completo y que es un caso particular del problema de la mochila. Reemplazamos los valores de v y w con k y por cada número creamos elementos donde su valor y peso son sigo mismo.

Subset Sum => Mochila:
Si existe una suma de números tal que dé k, entonces la suma de los valores de los elementos es también k, como los valores y pesos e aquellos elementos también es k. Por lo que entran en la mochila de capacidad k y tienen un valor mayor igual a k.

Mochila => Subset Sum:
Si podemos insertar elementos en la mochila tal que su suma sea mayor igual a v = k y menor e igual a w = k, entonces necesariamente estas sumas son igual a k. Entonces encontramos un subconjunto de números que suman a k.
"""
