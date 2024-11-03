# (★★★) En un hospital, se tiene un conjunto de médicos y un conjunto de pacientes. Cada médico tiene un horario con franjas horarias disponibles para citas médicas y su área de especialidad, y cada paciente tiene sus franjas horaria disponibles para ir al médico, junto con la información de qué tipo de especialidad requiere. Nuestro objetivo es emparejar médicos con pacientes de manera que se maximice el número total de citas médicas programadas. Se puede asumir que cada visita médica dura una cuota de tiempo fija, y que los pacientes pueden ser a priori atendidos por cualquier médico que coincida con el área de especialidad que requieren. Implementar un algoritmo que resuelva dicho problema de manera eficiente. Indicar y justificar la complejidad del algoritmo implementado.

from ..grafo import Grafo
from utils import encontrar_camino, actualizar_grafo_residual


class Medico:
    def __init__(self, nombre, horarios_disponibles, especialidad):
        self.nombre: str = nombre
        self.horarios: set = horarios_disponibles
        self.especialidad: str = especialidad


class Paciente:
    def __init__(self, nombre, horarios_disponibles, especialidad_requerida):
        self.nombre: str = nombre
        self.horarios: set = horarios_disponibles
        self.especialidad: str = especialidad_requerida


def ford_fulkerson(red: Grafo, s, t):
    flujos = {(v, w): 0 for v in red for w in red.adyacentes(v)}
    residual = red.copy()

    while (camino := encontrar_camino(residual, s, t)) is not None:
        for i in range(1, len(camino)):
            v = camino[i - 1]
            w = camino[i]

            if red.estan_unidos(v, w):
                flujos[(v, w)] += 1
            else:
                flujos[(v, w)] -= 1

            actualizar_grafo_residual(residual, v, w, 1)

    return flujos


def hospital(medicos: list[Medico], pacientes: list[Paciente]):
    red = Grafo(dirigido=True)
    red.agregar_vertice("fuente")
    red.agregar_vertice("sumidero")

    # O(m * h)
    for m in medicos:
        red.agregar_vertice(m)
        red.agregar_arista("fuente", m, 1)

        for hor in m.horarios:
            esp_hor = m.especialidad + hor
            if esp_hor not in red:
                red.agregar_vertice(esp_hor)

            red.agregar_arsita(m, esp_hor, 1)

    # O(p * h)
    for p in pacientes:
        red.agregar_vertice(p)
        red.agregar_arista(p, "sumidero", 1)

        for hor in p.horarios:
            esp_hor = p.especialidad + hor
            if esp_hor in red:
                red.agregar_arista(esp_hor, p, 1)

    # O((m + p + e * h) * (m + p + (e * h)^2))
    flujos = ford_fulkerson(red, "fuente", "sumidero")

    # O(m + p + e * h)
    grafo_match = Grafo(dirigido=True)
    for (v, w), f in flujos.items():
        if f == 0:
            continue

        if v not in grafo_match:
            grafo_match.agregar_vertice(v)
        if w not in grafo_match:
            grafo_match.agregar_vertice(w)

        grafo_match.agregar_arista(v, w, 1)

    # O(m * h * p)
    matcheos = {}
    for m in medicos:
        for esp_hor in grafo_match.get(m, []):
            for p in grafo_match.get(esp_hor, []):
                matcheos[m] = matcheos.get(m, []) + [p]

    return matcheos
