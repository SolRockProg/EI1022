def prod_max(K, N):
    def L(k, n):
        if k == 0: return 1
        if n == 0: return -float("infinity")
        if (k, n) not in mem:
            mem[k, n] = max((L(k - 1, n - d) * d, (k - 1, n - d, d)) for d in range(1, n+1))
        return mem[k, n][0]

    mem = {}
    score = L(K, N)
    k, n = K, N
    sol = []
    if score != -float("infinity"):
        while k != 0:
            k_prev, n_prev, d = mem[k, n][1]
            sol.append(d)
            k, n = k_prev, n_prev
        sol.reverse()
    return score, sol


if __name__ == "__main__":
    N = 12
    K = 3
    print(prod_max(K, N))
