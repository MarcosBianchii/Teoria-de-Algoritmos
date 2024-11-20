def mochila(elementos, w, k):
    def bt(i, optimo, mochila, valores, pesos):
        if i == len(elementos):
            return mochila.copy() if valores > sum(v for v, _ in optimo) else optimo

        if len(mochila) + len(elementos) - i < k:
            return optimo

        v, p = elementos[i]
        mochila.append((v, p))
        if pesos + p <= w:
            optimo = bt(i + 1, optimo, mochila, valores + v, pesos + p)

        mochila.pop()
        return bt(i + 1, optimo, mochila, valores, pesos)

    return bt(0, [], [], 0, 0)
