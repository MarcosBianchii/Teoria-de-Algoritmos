# (★) Implementar un algoritmo tipo Backtracking que reciba una cantidad de dados n y una suma s. La función debe devolver todas las tiradas posibles de n dados cuya suma es s. Por ejemplo, con n = 2 y s = 7, debe devolver[[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]]. ¿De qué complejidad es el algoritmo en tiempo? ¿Y en espacio?

def sumatoria_dados(n, s):
    """
    La complejidad temporal del algoritmo es O(2^n)
    """
    def sumas(resultados, dados, suma):
        if len(dados) == n and suma == s:
            resultados.append(dados.copy())
            return resultados

        if suma + 6 * (n - len(dados)) < s:
            return resultados

        tope = min(6, s - suma) + 1
        for i in range(1, tope):
            dados.append(i)
            sumas(resultados, dados, suma + i)
            dados.pop()

        return resultados

    return sumas([], [], 0)
