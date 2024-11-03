def tiro_con_arco(L):
    tiradores = {t: 0 for t, _ in L}

    def merge(izq, der):
        i, j, k = 0, 0, 0
        res = [0] * (len(izq) + len(der))

        while i < len(izq) and j < len(der):
            if izq[i][1] < der[j][1]:
                res[k] = izq[i]
                i += 1
            else:
                tiradores[izq[i][0]] += 1
                res[k] = der[j]
                j += 1

            k += 1

        while i < len(izq):
            res[k] = izq[i]
            i += 1
            k += 1

        while j < len(der):
            res[k] = der[j]
            j += 1
            k += 1

        return res

    def inversiones(a, b):
        if b - a <= 1:
            return L[a:b]

        medio = (a + b) // 2
        izq = inversiones(a, medio)
        der = inversiones(medio, b)
        return merge(izq, der)

    inversiones(0, len(L))
    return tiradores


L = [("A", 3), ("B", 4), ("C", 2), ("D", 8), ("E", 6), ("F", 5)]
print(tiro_con_arco(L))
