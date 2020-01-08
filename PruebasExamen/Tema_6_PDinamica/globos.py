def globos(H, vector_globos):
    def L(n, h):
        if n == 0: return 0
        if h > H: return -float("infinity")
        if (n, h) not in mem:
            if h <= vector_globos[n - 1][1]:
                mem[n, h] = max((L(n - 1, h), (n - 1, h, 0)),
                                (L(n - 1, vector_globos[n - 1][1]) + 1, (n - 1, vector_globos[n - 1][1], 1)))
            else:
                mem[n, h] = (L(n - 1, h), (n - 1, h, 0))
        return mem[n, h][0]

    mem = {}
    score = L(len(vector_globos), 0)
    n, h = len(vector_globos), 0
    sol = []
    while n != 0:
        n_previo, h_previo, d = mem[n, h][1]
        if d == 1:
            sol.append(n_previo)
        n, h = n_previo, h_previo
    sol.reverse()
    return sol, score


if __name__ == "__main__":
    vector = [(1, 2), (2.5, 3), (3, 2.5), (4.5, 2), (5, 3), (7, 1.5), (8, 3), (10, 0.5)]
    H = 4
    print(globos(H, vector))
