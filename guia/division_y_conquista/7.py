# (★★) Implementar un algoritmo que dados n puntos en un plano, busque la pareja que se encuentre más cercana, por división y conquista, con un orden de complejidad mejor que O(n ^ 2). Justificar el orden del algoritmo mediante el teorema maestro. Se puede asumir que ningún par de puntos tienen la misma coordenada x o y.

from math import inf


def puntos_mas_cercanos(puntos):
    """
    T(n) = aT(n/b) + O(n^c)

    a = 2
    b = 2
    c = 1

    log_b(a) = c -> T(n) = O(n^c logn) = O(nlogn)
    """
    def dist(p0, p1):
        # No computa la raiz, no es necesaria
        p, q = p0[0] - p1[0], p0[1] - p1[1]
        return p ** 2 + q ** 2

    def partir_en_lados(ps, xa):
        Qs, Rs = [], []
        for p in ps:
            Ss = Qs if p[0] <= xa else Rs
            Ss.append(p)

        return Qs, Rs

    def puntos_mas_cercanos_rec(px, py):
        if len(px) <= 3:
            pps = []
            for i in range(1, len(px)):
                for j in range(i):
                    pps.append((px[i], px[j]))

            return min(pps, key=lambda p: dist(p[0], p[1]))

        mid = len(px) // 2
        xa = px[mid - 1][0]
        Qx, Rx = partir_en_lados(px, xa)
        Qy, Ry = partir_en_lados(py, xa)

        q0, q1 = puntos_mas_cercanos_rec(Qx, Qy)
        r0, r1 = puntos_mas_cercanos_rec(Rx, Ry)
        d = min(dist(q0, q1), dist(r0, r1))

        Sy = [p for p in py if dist(p, (xa, p[1])) <= d]

        dmin, ssmin = inf, (None, None)
        for i, p in enumerate(Sy):
            a = i + 1
            b = min(i + 16, len(Sy))
            for q in map(lambda j: Sy[j], range(a, b)):
                d = dist(p, q)
                if d <= dmin:
                    dmin = d
                    ssmin = p, q

        return min(ssmin, (q0, q1), (r0, r1), key=lambda ps: dist(ps[0], ps[1]))

    px = sorted(puntos, key=lambda p: p[0])
    py = sorted(puntos, key=lambda p: p[1])
    return puntos_mas_cercanos_rec(px, py)
