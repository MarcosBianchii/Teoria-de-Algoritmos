from random import randint
from sys import argv


if __name__ == "__main__":
    """
    n: Cantidad de filas
    m: Cantidad de columnas
    k: Cantidad de barcos
    a-b: Rango de numeros aleatorios para las restricciones
    p-q: Rango de numeros aleatorios para los barcos
    """
    if len(argv) < 6:
        print(f"Uso: {argv[0]} <n> <m> <k> <a-b> <p-q>")
        exit(1)

    n = int(argv[1])
    m = int(argv[2])
    k = int(argv[3])
    a, b = tuple(map(int, argv[4].split("-")))
    p, q = tuple(map(int, argv[5].split("-")))

    datos = []
    for _ in range(n):
        datos.append(randint(a, b))

    datos.append("")
    for _ in range(m):
        datos.append(randint(a, b))

    datos.append("")
    for _ in range(k):
        datos.append(randint(p, q))

    for num in datos:
        print(num)
