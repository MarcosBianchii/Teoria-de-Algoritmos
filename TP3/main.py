from sys import argv
from codigo.bt import batalla_naval as batalla_naval_bt
from codigo.pl import batalla_naval as batalla_naval_pl
from codigo.greedy import batalla_naval as batalla_naval_gr
from codigo.aprox import batalla_naval as batalla_naval_aprox
from codigo.util import restricciones_from_archivo, print_tablero

if __name__ == "__main__":
    msg_uso = f"Uso: python3 {argv[0]} <bt | pl | aprox | gr> <path a archivo>"

    if len(argv) != 3:
        print(msg_uso)
        exit(1)

    metodo = argv[1].lower()
    resolver = {
        "bt": batalla_naval_bt,
        "pl": batalla_naval_pl,
        "gr": batalla_naval_gr,
        "aprox": batalla_naval_aprox,
    }

    if metodo not in resolver:
        print(msg_uso)
        exit(1)

    path = argv[2]
    filas, columnas, b = restricciones_from_archivo(path)
    total = sum(filas) + sum(columnas)

    tablero, cumplida = resolver[metodo](filas, columnas, b)
    print_tablero(tablero, filas, columnas)
    print(f"\ncumplido: {cumplida}\ntotal: {total}")
