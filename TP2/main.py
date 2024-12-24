from sys import argv
from codigo.algoritmo import jugar

if __name__ == "__main__":
    if len(argv) != 2:
        print(f"Uso: python3 {argv[0]} <path a monedas>")
        exit(1)

    path = argv[1]
    with open(path) as f:
        monedas = [int(n) for n in f.read().split(";")]

    Gs, Gm, elecciones = jugar(monedas)

    print("; ".join(elecciones))
    print(f"Ganancia Sophia: {Gs}")
    print(f"Ganancia Mateo: {Gm}")
