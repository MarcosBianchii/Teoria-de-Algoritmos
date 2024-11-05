def maximo_sub_arreglo(numeros):
    def expandir_suma(a, mid, b):
        menor_a = mid
        optimo = 0
        suma = 0
        for i in range(mid - 1, a - 1, -1):
            suma += numeros[i]
            if suma > optimo:
                menor_a = i
                optimo = suma

        mayor_b = mid + 1
        optimo = 0
        suma = 0
        for i in range(mid, b):
            suma += numeros[i]
            if suma > optimo:
                mayor_b = i + 1
                optimo = suma

        return numeros[menor_a:mayor_b]

    def dyc(a, b):
        if b - a == 1:
            return numeros[a:b]

        mid = (a + b) // 2
        izq = dyc(a, mid)
        der = dyc(mid, b)
        med = expandir_suma(a, mid, b)
        return max(izq, med, der, key=sum)

    return dyc(0, len(numeros))
