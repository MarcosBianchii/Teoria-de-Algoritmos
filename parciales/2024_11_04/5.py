def osvaldo(p):
    def dyc(a, b):
        if b - a == 1:
            return 0, a, a

        mid = (a + b) // 2
        g_izq, a_izq, b_izq = dyc(a, mid)
        g_der, a_der, b_der = dyc(mid, b)
        g_med = p[b_der] - p[a_izq]

        if max(g_izq, g_der, g_med) == g_med:
            return g_med, a_izq, b_der
        elif g_izq > g_der:
            return g_izq, a_izq, b_izq
        else:
            return g_der, a_der, b_der

    return dyc(0, len(p))
