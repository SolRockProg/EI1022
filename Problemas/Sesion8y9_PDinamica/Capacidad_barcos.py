def peso_maximo_barco(w, P, N):
    def L(p, n):
        if n == 0: return 0
        if (p, n) not in mem:
            if p >= w[n - 1]:
                mem[p, n] = max((L(p - w[n - 1], n - 1) + w[n - 1], (p - w[n - 1], n - 1, 1)),
                                (L(p, n - 1), (p, n - 1, 0)))
            else:
                mem[p, n] = L(p, n - 1), (p, n - 1, 0)
        return mem[p, n][0]

    mem = {}
    score = L(P, N)
    sol = []
    p, n = P, N
    while n != 0:
        p_prev, n_prev, d = mem[p, n][1]
        if d==1: sol.append(w[n_prev])
        p, n = p_prev, n_prev
    sol.reverse()
    return score, sol


if __name__ == "__main__":
    w = [4, 3, 3, 2, 2]
    P = 16
    N = len(w)
    print(peso_maximo_barco(w, P, N))
