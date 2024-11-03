# (★★) En el reino de Gondor ha incrementado enormemente la delincuencia luego de su urbanización. El rey Aragorn no quiere que todo su esfuerzo en construir calles resulte en vano, por lo que quiere poner guardianes a vigilar las calles por las noches. El problema es que cuesta mucho dinero entrenar a dichos guardianes, por lo que quiere reducir al mínimo la cantidad que sean necesarios entrenar. Sabe que cada guardian puede estar vigilando desde una esquina, y desde allí tener visibilidad hasta cualquier otra esquina directa. Necesita determinar la cantidad mínima de guardianes que son necesarios para cubrir todas las calles de su reino. Como primera medida, consulta con el oráculo Discipulus Theoriae Algoritmi (es decir, quien lee esta consigna), para determinar si esto es conseguible en corto tiempo (el oráculo le pregunó algo sobre tiempo polinomial, que Aragorn no entendió y le dijo “si, eso”). Tenemos que explicarle a Aragorn que este pedido no es realizable (y debe armarse de paciencia, o no buscar el mínimo exacto), porque el problema de Guardianes de Gondor es, en realidad, un problema NP-Completo (en su versión de problema de decisión: “¿Se pueden vigilar todas las calles con esta topología con un máximo de K guardianes?”).

"""
El problema de Aragorn es basicamente el problema de Vertex Cover, donde cada esquina representa un vértice en un grafo y las calles son sus aristas. El conjunto de cubrimiento representa donde sí y donde no hay que posicionar a los guardianes para cubrir todas las calles.

Problema de decisión de Vertex Cover:
Dado un grafo y un número entero `k`, determinar si es posible obtener un subconjunto de vértices tales que para todas las aristas del grafo algúno de sus extremos esté en este conjunto.

Problema de decisión del problema de Aragorn:
Dado el mapa (en forma de diccionarios) de una ciudad de Gondor y un número entero `k`, determinar si es posible cubrir todas las calles del reino utilizando a lo sumo k guardianes.
"""


def verificador_aragorn(esquinas, k, posiciones):
    """
    La complejidad del verificador es O(esquinas + calles)
    """
    if len(posiciones) > k:
        return False

    # O(posiciones)
    if any(p not in esquinas for p in posiciones):
        return False

    # O(esquinas + calles)
    for e in esquinas:
        for a in esquinas[e]:
            if e not in posiciones and a not in posiciones:
                return False

    return True


"""
Como la complejidad del verificador es polinómica, el problema de Aragorn está en NP.

    def vertex_cover(grafo, k):
        # transformacion
        return aragorn(mapa, k)

Como el enunciado no especifica cual es el formato del mapa del problema de Aragorn, entonces decido que va a ser un grafo. La transformación no existe, es de hecho el mismo problema, no hace falta modelar nada.

VC => Aragorn:
Si existe un Vertex Cover de por lo menos k vértices, entonces, en este mismo grafo, como los vértices representan esquinas y podemos garantizar que podemos cubrir todas las calles, entonces podemos cubrir todas las calles con k guardianes.

Aragorn => VC:
Si existe una forma de ubicar a como mínimo k guardianes en las esquinas de Gondor de forma tal que todas las calles tengan por lo menos a un guardian asignado. Entonces en el mismo grafo, existe una forma de elegir k vértices tal que cubran todas las aristas.
"""
