def suma_producto_maximo(listas, S):
    def L(n, s):
        if n == 0 and s == 0: return 1
        if n == 0: return -float("infinity")
        if (n, s) not in mem:
            mem[n, s] = float("-inf"), ()
            for d in listas[n - 1]:
                if s >= d:
                    mem[n, s] = max(mem[n, s], (L(n - 1, s - d) * d, (n - 1, s - d, d)))
        return mem[n, s][0]

    mem = {}
    score = L(len(listas), S)
    n, s = len(listas), S
    res = []
    while n != 0:
        n_previo, s_previo, d = mem[n, s][1]
        res.append(d)
        n, s = n_previo, s_previo
    res.reverse()
    return res, score


if __name__ == "__main__":
    S = 14
    lista = [[4, 2], [10, 6], [8, 2]]
    print(suma_producto_maximo(lista, S))
