# (★) Realizar un seguimiento de aplicar el Algoritmo de Huffman al texto “PRETERINTENCIONALIDAD”, indicando el binario resultante de comprimirlo. ¿Por qué se trata de un algoritmo Greedy? Justificar

"""
x = "PRETERINTENCIONALIDAD"

# Armamos un heap minimal con las letras y sus frecuencias
characters = Counter(x)
heap = heapify([(freq, ch) for ch, freq in characters])

# Ahora tomamos los 2 primeros elementos y formamos
# un nodo tomando la suma de sus frecuencias.
while len(heap) > 1:
    l = heappop(heap)
    r = heappop(heap)
    heappush(Node(l, r))

# Aca devuelve la raiz del arbol
return heap[0]

De esta forma obtenemos el arbol de huffman que para este caso en particular queda de la siguiente manera

                   21
         +---------+---------+
         8                   13
    +----+----+          +---+---+
    4         4          7       6
  +-+-+     +-+-+      +-+-+   +-+-+
  A   2     D   2      4   E   I   N
    +-+-+     +-+-+  +-+-+
    P   C     O   L  R   T

Tomando la convencion donde los 0 son la izquierda y 1 la derecha, la compresion resultante es:

P    R    E   T    E   R    I   N   T    E   N   C    I   O    N   A   L    I   D   A   D
0010 1000 101 1001 101 1000 110 111 1001 101 111 0011 110 0110 111 000 0111 110 010 000 010

Resultado: 00101000101100110110001101111001101111001111001101110000111110010000010 (71 bits)
PRETERINTENCIONALIDAD son 21 bytes = 168 bits

El algoritmo es greedy porque mediante varias iteraciones forma un arbol minimizando el costo en bites de aquellos caracteres que mas aparecen. Utiliza una regla simple, tomar siempre los nodos de menor costo para formar otro y volver a meterlo en el heap. De esta forma alcanza la solucion optima de comprimir el mensaje original en una cadena de 0s y 1s.
"""
