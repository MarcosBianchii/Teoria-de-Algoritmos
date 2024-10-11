# (★) Explicar para cada uno de los siguientes casos, qué modificaciones se deben aplicar sobre una red para convertirla en una red de flujo apta para la utilización del algoritmo de Ford-Fulkerson.

# a. En la red existen bucles.

# b. En la red hay ciclos de dos vértices (aristas antiparalelas).

# c. En la red hay más de una fuente.

# d. En la red hay más de un sumidero.

"""
a)
Se sacan, no aportan nada.

b)
Crear un vertice intermedio que ocupe alguna de las aristas.

    A -> B
    B -> A

Pasaria a ser

    A -> C
    C -> B
    B -> A

Estas nuevas aristas tienen la misma capacidad que la anterior.

c)
Se crea un vertice fuente nuevo que conecte a las fuentes anteriores. Si S1 y S2 son fuentes entonces creamos S' tal que existan S'->S1 y S'->S2 con capacidades iguales a la suma de las capacidades de los arcos salientes de ellos.

d)
Analogo que con las fuentes, se agrega un nuevo vertice que actue como sumidero de los sumideros actuales donde para cada uno se agrega una arista saliente hacia el nuevo con capacidad igual a la suma de las capacidades arcos entrantes de ellos.

"""
