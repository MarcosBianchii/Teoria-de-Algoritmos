# (★) Se tiene una lista de materias que deben ser cursadas en el mismo cuatrimestre, cada materia está representada con una lista de cursos/horarios posibles a cursar (solo debe elegirse un horario por cada curso). Cada materia puede tener varios cursos. Implementar un algoritmo de backtracking que devuelva un listado con todas las combinaciones posibles que permitan asistir a un curso de cada materia sin que se solapen los horarios. Considerar que existe una función son_compatibles(curso_1, curso_2) que dados dos cursos devuelve un valor booleano que indica si se pueden cursar al mismo tiempo.


def son_compatibles(a, b):
    pass


def obtener_combinaciones(materias):
    if not materias:
        return []

    def verificar_compatibilidad(ocupado, nueva):
        if not ocupado:
            return True

        for materia in ocupado:
            if not son_compatibles(materia, nueva):
                return False

        return True

    combinaciones = []

    def obtener_combinaciones_rec(i, ocupado):
        if len(materias) == len(ocupado):
            combinaciones.append(ocupado.copy())
            return

        for cursos in materias[i]:
            if verificar_compatibilidad(ocupado, cursos):
                ocupado.append(cursos)
                obtener_combinaciones_rec(i + 1, ocupado)
                ocupado.pop()

    obtener_combinaciones_rec(0, [])
    return combinaciones
