# Ejecución del programa

```sh
python3 main.py <bt | pl | aprox | gr> <path>
```

El programa recibe un método para resolver el algoritmo y un path a un archivo que sigue un cierto formato donde en cada linea del archivo hay un número, el primer conjunto de números son las restricciones por fila, luego las de columnas y por último van los barcos a usar. Todos estos están separados por una linea vacia.

Un ejemplo es:

```
3
3

2
1

2
2
```

Donde en este caso nos queda un tablero de `2x2` donde en cada fila hay una demanda de `3`, en la primer columna hay de `2` y en la segunda `1`, y hay `2` barcos de largo `2`.

Va a resolver el problema usando la técnica de programación especificada por parámetro y va a imprimir un tablero mostrando las posiciones escogidas por el algoritmo y la cantidad de demanda cumplida.
