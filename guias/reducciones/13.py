# (★★) Realizar una reducción polinomial del siguiente problema a otro de los vistos durante la cursada. Ayuda: pensar en alguno de los vistos de programación dinámica. Dada esta reducción, ¿se puede afirmar que este problema es NP-Completo?

# Dado un número n, encontrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados.

"""
Problema de decisión:
Dado un número n y un entero `k`, determinar si el número n puede ser escrito como una suma de cuadrados tal que esta suma tenga como máximo k términos.

Propongo el problema del cambio que es NP-Completo.

Problema de decicisión del problema del Cambio:
Dada una colección de monedas, un valor `v` y un entero `k`, determinar si es posible usar a lo sumo k monedas para alcanzar el valor v.
"""

from math import sqrt


def verificador(n, k, terminos):
    """
    La complejidad del verificador es O(n)
    """
    if len(terminos) > k:
        return False

    # O(n)
    if sum(terminos) != n:
        return False

    # O(n)
    for t in terminos:
        if not sqrt(t).is_integer():
            return False

    return True


"""
Como la complejidad del verificador es polinómica, entonces el problema está en NP.

    def problema(n, k):
        # transformacion
        return cambio(monedas, n, k)

Podemos generar el arreglo de monedas utilizando cuadrádos perfectos hasta alcanzar n (inclusive). Utilizando estos valores, queremos alcanzar el valor de n, utilizando a lo sumo k monedas, estas representan los términos. Como los valores son solo positivos, en caso de pasarnos con la suma, no podemos vovler, por lo que generar números más grandes que n es redundante.

Por definición de problema NP-Completo, este problema en NP, es reducible al problema del cambio, si quisieramos probar que es también NP-Completo, entonces habría que reducir el problema del cambio a este particular, por lo que de momento no podemos asegurar que este sea NP-Completo.
"""
