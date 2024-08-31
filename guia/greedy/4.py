# (★★) Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. Implementar un algoritmo Greedy que reciba el arreglo de los horarios de las charlas, representando en tuplas los horarios de inicios de las charlas, y sus horarios de fin, e indique cuáles son las charlas a dar para maximizar la cantidad total de charlas. Indicar y justificar la complejidad del algoritmo implementado.

def charlas(horarios):
    """
    La complejidad del algoritmo es O(nlogn)
    """
    def se_solapan(h1, h2):
        # Sabemos que siempre f1 <= f2
        # i1 ----- i2 ------ f1 --- f2
        return h2[0] <= h1[1]

    if len(horarios) == 0:
        return []

    # O(nlogn)
    horarios.sort(key=lambda x: x[1])

    # O(n)
    charlas = [horarios[0]]
    for i in range(1, len(horarios)):
        horario = horarios[i]
        if not se_solapan(charlas[-1], horario):
            charlas.append(horario)

    return charlas
