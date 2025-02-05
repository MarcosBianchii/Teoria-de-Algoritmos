def juan_no_tan_vago(trabajos):
    """
    juan_el_vago:
    f(n) = max(f(n - 2) + g[n], f(n - 1))

    f(n) = max(f(n - 3) + g[n - 1] + g[n], f(n - 2) + g[n], f(n - 1))

    opt[i] = max(opt[i-1], g[i-1] + opt[i-2], g[i-1] + g[i-2] + opt[i-3])

    """
    n = len(trabajos)
    g = [0] + trabajos
    mem = [0] * (n + 1)

    mem[1] = g[1]
    mem[2] = g[1] + g[2]

    for i in range(3, n + 1):
        mem[i] = max(mem[i - 3] + g[n - 1] + g[n],
                     mem[i - 2] + g[n], mem[i - 1])

    return mem[i]
