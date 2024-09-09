# (★★) Se sabe, por el teorema de Bolzano, que si una función es continua en un intervalo [a, b], y que en el punto a es positiva y en el punto b es negativa (o viceversa), necesariamente debe haber (al menos) una raíz en dicho intervalo. Implementar una función raiz que reciba una función (univariable) y los extremos mencionados a y b, y devuelva una raíz dentro de dicho intervalo (si hay más de una, simplemente quedarse con una). La complejidad de dicha función debe ser logarítmica del largo del intervalo [a, b]. Asumir que por más que se esté trabajando con números enteros, hay raíz en dichos valores: Se puede trabajar con floats, y el algoritmo será equivalente, simplemente se plantea con ints para no generar confusiones con la complejidad. Justificar la complejidad de la función implementada.


def raiz(funcion, a, b):
    """
    T(n) = aT(n/b) + O(n^c)

    a = 1
    b = 2
    c = 0 considerando que evaluar `funcion` es O(1)

    log_b(a) = c -> T(n) = O(n^c logn) = O(logn)
    """
    p = (a + b) // 2
    fafp = funcion(a) * funcion(p)

    if fafp > 0:
        a = p
    elif fafp < 0:
        b = p
    else:
        return p

    return raiz(funcion, a, b)
