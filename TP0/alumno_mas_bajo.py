# La Escuela Nacional 32 "Alan Turing" de Bragado tiene una forma particular de requerir que los alumnos formen fila. En vez del clásico "de menor a mayor altura", lo hacen primero con alumnos yendo con altura decreciente, hasta llegado un punto que empieza a ir de forma creciente, hasta terminar con todos los alumnos.

# Por ejemplo las alturas podrían ser 1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 1.18, 1.23.

# Implementar una función indice_mas_bajo que dado un arreglo/lista de alumnos(*) que represente dicha fila, devuelva el índice del alumno más bajo, en tiempo logarítmico. Se puede asumir que hay al menos 3 alumnos. En el ejemplo, el alumno más bajo es aquel con altura 0.98.

# Implementar una función validar_mas_bajo que dado un arreglo/lista de alumnos(*) y un índice, valide (devuelva True o False) si dicho índice corresponde al del alumno más bajo de la fila. (Aclaración: esto debería poder realizarse en tiempo constante)

# (*)
# Los alumnos son de la forma:

# alumno {
#     nombre (string)
#     altura (float)
# }
# Se puede acceder a la altura de un alumno haciendo varible_tipo_alumno.altura.

# Importante: considerar que si la prueba de volumen no pasa, es probable que sea porque no están cumpliendo con la complejidad requerida.


def alturas(alumnos, i):
    izq = alumnos[i - 1].altura
    mid = alumnos[i].altura
    der = alumnos[i + 1].altura
    return izq, mid, der


def indice_mas_bajo(alumnos):
    a = 0
    b = len(alumnos)

    while True:
        mid = (a + b) >> 1
        altura_izq, altura_mid, altura_der = alturas(alumnos, mid)

        if altura_der < altura_mid:
            a = mid + 1
        elif altura_izq < altura_mid:
            b = mid
        else:
            return mid


def validar_mas_bajo(alumnos, indice):
    altura_izq, altura_mid, altura_der = alturas(alumnos, indice)
    return min(altura_izq, altura_mid, altura_der) == altura_mid
