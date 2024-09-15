# (★) Es el año 1700, y la pirata Barba-ra Verde atacó un barco de la Royal British Shipping & Something, que transportaba una importante piedra preciosa de la corona británica. Al parecer, la escondieron en un cofre con muchas piedras preciosas falsas, en caso de un ataque. Barba-ra Verde sabe que los refuerzos británicos no tardarán en llegar, y deben huir lo más rápido posible. El problema es que no pueden llevarse el cofre completo por pesar demasiado. Necesita encontrar rápidamente la joya verdadera. La única forma de descubrir la joya verdadera es pesando. Se sabe que la joya verdadera va a pesar más que las imitaciones, y que las imitaciones pesan todas lo mismo. Cuenta con una balanza de platillos para poder pesarlas(es el 1700, no esperen una balanza digital).

# a. Escribir un algoritmo de división y conquista, para determinar cuál es la verdadera joya de la corona. Suponer que hay una función balanza(grupo_de_joyas1, grupo_de_joyas2) que devuelve 0 si ambos grupos pesan lo mismo, mayor a 0 si el grupo1 pesa más que el grupo2, y menor que 0 si pasa lo contrario, y realiza esto en tiempo constante.

# b. Indicar y justificar (adecuadamente) la complejidad de la función implementada.

def balanza(j1, j2):
    """
    Se asume que es de tiempo constante
    """
    return sum(j1) - sum(j2)


def encontrar_joya(joyas):
    """
    T(n) = aT(n/b) + O(n^c)

    a = 1
    b = 2
    c = 1 <- Por crear slices

    log_b(a) < c -> T(n) = O(n^c) = O(n)
    """
    def encontrar_joya_rec(a, b):
        if b - a == 1:
            return a

        mid = (a + b) // 2
        if (b - a) % 2 == 0:
            bal = balanza(joyas[a:mid], joyas[mid:b])
        else:
            bal = balanza(joyas[a:mid], joyas[mid + 1:b])
            if bal == 0:
                return mid

        if bal == 1:
            b = mid
        elif bal == -1:
            a = mid + (b - a) % 2

        return encontrar_joya_rec(a, b)

    return encontrar_joya_rec(0, len(joyas))
