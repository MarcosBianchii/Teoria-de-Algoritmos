from sys import argv, stderr, stdout
from random import randint

"""
Genera un juego de N monedas donde A y B representan el intervalo de
numeros pseudo-aleatorios para sus valores.

Escribe el resultado por stdout separando los valores con `;`.
"""


if __name__ == "__main__":
    if len(argv) != 4:
        print(f"Uso: {argv[0]} <N:int> <A:int> <B:int>", file=stderr)
        exit(1)

    try:
        cantidad_de_monedas = int(argv[1])
        a = int(argv[2])
        b = int(argv[3])
    except ValueError:
        print("Los parametros deben ser enteros", file=stderr)
        exit(1)

    if b < a:
        print("Los numeros estan mal ordenados", file=stderr)
        exit(1)

    if a < 0:
        print("Los numeros no pueden ser negativos", file=stderr)
        exit(1)

    escritos = 0
    numeros = []
    for _ in range(cantidad_de_monedas):
        r = randint(a, b)
        numeros.append(r)
        if len(numeros) == 100:
            string = ";".join(map(str, numeros))
            if escritos < cantidad_de_monedas:
                string += ";"

            stdout.write(string)
            escritos += len(numeros)
            numeros.clear()

    stdout.write(";".join(map(str, numeros)) + "\n")
