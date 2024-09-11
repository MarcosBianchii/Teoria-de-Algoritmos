# (★★) Se tiene una colección de n libros con diferentes espesores, que pueden estar entre 1 y n (valores no necesariamente enteros). Tu objetivo es guardar esos libros en la menor cantidad de cajas. Todas las cajas disponibles son de la misma capacidad L (se asegura que L≥n). Obviamente, no podés partir un libro para que vaya en múltiples cajas, pero sí podés poner múltiples libros en una misma caja, siempre y cuando los espesores no superen esa capacidad L. Implementar un algoritmo Greedy que obtenga las cajas, tal que se minimicen la cantidad de cajas a utilizar. Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. ¿El algoritmo propuesto encuentra siempre la solución óptima? Justificar. ¿Qué cambios aplicarías si supieras que los espesores sólo fueran números enteros de un rango acotado? Describir cómo afecta a la complejidad, y a su optimalidad.

def cajas(capacidad, libros):
    """
    Este algoritmo no siempre encuentra la solucion optima. Un contra ejemplo es
        - capacidad: 5
        - libros: [3, 5, 2, 4, 1]

    Donde la solucion optima es [[5], [4, 1], [3, 2]] pero este algoritmo encuentra
    [[5], [4], [3, 2], [1]].

    El algoritmo es Greedy porque sigue una regla sencilla donde en cada iteracion
    busca guardar el libro de mayor espesor, de no entrar en la ultima caja (es la
    que tiene mas espacio disponible), entonces toma una caja nueva y comienza a
    llenarla. 

    La complejidad del algoritmo es O(nlogn)
    """
    if not libros:
        return []

    # O(nlogn)
    libros.sort(reverse=True)

    # O(n)
    cajas = [[]]
    for libro in libros:
        caja = cajas[-1]
        if sum(caja) + libro <= capacidad:
            caja.append(libro)
        else:
            cajas.append([libro])

    return cajas
