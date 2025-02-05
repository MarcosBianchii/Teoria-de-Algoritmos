from sys import argv
from codigo.validador import validador_batalla_naval
from codigo.util import restricciones_from_archivo, tablero_from_archivo

"""
Dada la entrada: `ejemplos/3_3_2.txt`
asume que existe: `ejemplos/tableros/3_3_2.txt`
"""

if __name__ == "__main__":
    err_msg = f"Uso: python3 {argv[0]} <path a archivo>"

    if len(argv) != 2:
        print(err_msg)
        exit(1)

    path = argv[1]

    # Armar el path al tablero
    path_tablero = path.split("/")
    path_tablero.insert(1, "tableros")
    path_tablero = "/".join(path_tablero)

    filas, columnas, b = restricciones_from_archivo(path)
    tablero = tablero_from_archivo(path_tablero)
    print(validador_batalla_naval(filas, columnas, b, tablero))
