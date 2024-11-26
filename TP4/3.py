# Implementar un algoritmo que "acepte" el mismo lenguaje que el siguiente Autómata Finito Determinista. Es decir, implementar una función `es_parte_lenguaje` que reciba una cadena y devuelva True si la cadena forma del lenguaje del siguiente autómata. La función debe ejecutar en tiempo CONSTANTE. Se garantiza que la cadena solamente contiene como posibles símbolos a, b y c.

def es_parte_lenguaje(cadena):
    if len(cadena) < 2:
        return False

    if cadena[:2] == "ac":
        return True

    if cadena[-2:] == "ab":
        return True

    return False
