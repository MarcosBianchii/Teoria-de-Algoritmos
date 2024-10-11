import sys
import os
from codigo.juego import jugar

RUTA_EJEMPLOS = "ejemplos/"
ARCHIVO_RESULTADOS = "resultados.txt"


def armar_fila(ruta):
    '''
    Recibe una ruta de archivo y devuelve una lista de enteros
    '''
    return [int(x) for x in open(ruta).read().split(';')]


def imprimir_resultados(archivo, ganancia_sophia, ganancia_mateo, ganancia_esperada=None):
    '''
    Imprime los resultados del juego 
    '''
    print(f"> Archivo: {archivo}")
    print(f"    Ganancia de Mateo: {ganancia_mateo}")
    print(f"    Ganancia de Sophia: {ganancia_sophia}")
    if ganancia_esperada:
        print(f"              esperada: {ganancia_esperada}")

    if ganancia_sophia > ganancia_mateo:
        print("    Ganó Sophia")
    elif ganancia_sophia == ganancia_mateo:
        print("    Empate")
    else:
        print("    Ganó Mateo")

    print()


def ejecutar_ejemplos():
    '''
    Ejecuta los ejemplos de la carpeta ejemplos e imprime los resultados obtenidos
    '''
    dir = os.fsencode(RUTA_EJEMPLOS)
    resultados = {}

    # Leer posibles resultados
    with open(RUTA_EJEMPLOS + ARCHIVO_RESULTADOS) as f:
        for line in f:
            if '.txt' in line:
                archivo = line.strip()

                while 'Ganancia de Sophia' not in line:
                    line = f.readline()

                resultados[archivo] = int(line.split(': ')[1])

    # Ejecutar ejemplos
    for file in os.listdir(dir):
        archivo = os.fsdecode(file)

        if archivo in resultados:
            ruta = RUTA_EJEMPLOS + archivo
            monedas = armar_fila(ruta)
            ganancia_sophia, ganancia_mateo = jugar(monedas)
            imprimir_resultados(archivo, ganancia_sophia,
                                ganancia_mateo, resultados[archivo])


def main(argv):
    if len(argv) == 1:
        ejecutar_ejemplos()
        return

    archivo = argv[1]
    monedas = armar_fila(RUTA_EJEMPLOS + archivo)
    ganancia_sophia, ganancia_mateo = jugar(monedas)

    imprimir_resultados(archivo, ganancia_sophia, ganancia_mateo)


if __name__ == '__main__':
    main(sys.argv)
