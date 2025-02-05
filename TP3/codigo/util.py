from concurrent.futures import ProcessPoolExecutor, as_completed
from math import log10, floor
import time
import os

# Este parámetro controla cuantas veces se ejecuta el algoritmo para cada
# tamaño. Esto es conveniente para reducir el error estadístico en la medición
# de tiempos. Al finalizar las ejecuciones, se promedian los tiempos obtenidos
RUNS_PER_SIZE = 4

# Ajustar este valor si se quiere usar más de un proceso para medir los tiempos
# de ejecución, o None para usar todos los procesadores disponibles. Si se usan
# varios procesos, tener cuidado con el uso de memoria del sistema.
MAX_WORKERS = (os.cpu_count() or 4)


def _time_run(algorithm, *args):
    start = time.time()
    algorithm(*args)
    return time.time() - start


def time_algorithm(algorithm, nm, k, get_args):
    futures = {}
    total_times = {(i, j): 0 for i in nm for j in k}

    # Usa un ProcessPoolExecutor para ejecutar las mediciones en paralelo
    # (el ThreadPoolExecutor no sirve por el GIL de Python)
    with ProcessPoolExecutor(MAX_WORKERS) as p:
        for i in nm:
            for j in k:
                for _ in range(RUNS_PER_SIZE):
                    fut = p.submit(_time_run, algorithm, *get_args(i, j))
                    futures[fut] = (i, j)

        for f in as_completed(futures):
            result = f.result()
            i, j = futures[f]
            total_times[(i, j)] += result

    return {(i, j): t / RUNS_PER_SIZE for (i, j), t in total_times.items()}


def restricciones_from_archivo(path):
    """
    filas, columnas, barcos
    """
    cosas, i = ([], [], []), 0
    with open(path) as f:
        for linea in f.readlines():
            sin_espacios = linea.strip()
            if len(sin_espacios) == 0:
                i += 1
            else:
                cosas[i].append(int(sin_espacios))

    return cosas


def tablero_from_archivo(path):
    tablero = []
    with open(path) as f:
        for fila in f.readlines():
            fila_tablero = []
            celdas = fila.split("   ")

            for celda in map(str.strip, celdas):
                fila_tablero.append(1 if celda != "-" else 0)

            tablero.append(fila_tablero)

    return tablero


def print_tablero(tablero, filas, columnas):
    def digitos(n):
        return int(log10(floor(max(1, n))) + 1)

    max_digitos_fila = digitos(max(filas))
    for i, row in enumerate(tablero):
        print("[ ", end="")
        for j, x in enumerate(row):
            casillero = [" "] * digitos(columnas[j])
            if bool(x):
                casillero[len(casillero) // 2] = "X"
                print("".join(casillero), end=" ")
            else:
                print("".join(casillero), end=" ")

        espacios = max_digitos_fila - digitos(filas[i])
        print("] " + " " * espacios + f"{filas[i]}")

    print("  ", end="")
    for c in columnas:
        print(str(c), end=" ")
    print()
