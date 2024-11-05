def contar_cambios(monedas, w):
    mem = [0] * (w + 1)
    mem[0] = 1

    for i in range(1, w + 1):
        mem[i] = sum(mem[i - m] for m in monedas if m <= i)

    print(mem)
    return mem[w]


monedas = [1, 2, 3]
w = 5
print(contar_cambios(monedas, w))

"""
1, 1, 1, 1, 1
1, 1, 1, 2
1, 2, 2
1, 1, 3
2, 3
"""
