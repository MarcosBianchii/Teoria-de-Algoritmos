# (★★) Definir el problema de decisión de las N-Reinas. Usar que N-Reinas es un problema NP-Completo para demostrar que Independent Set es un problema NP-Completo.

"""
El problema de decisión de N-Reinas es:
Dado un tablero de NxN, determinar si es posible posicionar exactamente N reinas de forma tal que ninguna amenaze a otra siguiendo las reglas del ajedrez donde una reina puede comer en cualquier dirección.

Para demostrar que Independent Set es NP-Completo podemos demostrar que N-Reinas es reducible a Independent Set, de esta forma demostrariamos que N-Reinas es a lo sumo tán dificil como Independent Set e Independent Set es por lo menos tán dificil como resolver N-Reinas, como N-Reinas es NP-Completo, estaríamos demostrando que Independent Set también lo es. No hace falta demostrar que N-Reinas está en NP, está el verificador eficiente en 5.py.

    def n_reinas(n):
        # transformacion
        return IS(grafo, n)

Podemos modelar el grafo tal que cada casillero tenga un vértice y exista una arista entre vértices si uno puede amenazar al otro en caso de tener una reina.

n reinas no se amenazan sii existe un Independent Set de tamaño n en el grafo modelado.

N-Reinas => IS:
Si existen n reinas que no se amenazan, en el grafo modelado representan vértices que por definición no estarían conectados, pues la condición por la que exista una arista entre ellos sería que sí se amenazaran. De esta forma existe un Independent Set de tamaño k si existen n reinas que no se amenazan en el tablero original.

IS => N-Reinas:
Si existe un Independent Set de n vértices en el grafo modelado, podemos asegurar que existan por lo menos n reinas no amenazadas en el tablero original, pues si no fuera así, las reinas se amenazarían, lo que diría que los vértices a las que se correspondían eran adyacentes, pero, eran parte de un Independent Set, por lo que es absurdo. 
"""
