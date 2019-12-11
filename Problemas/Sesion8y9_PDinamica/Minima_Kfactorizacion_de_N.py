def sum_min(K, N):
    def L(k, n):
        if k == 0: return n
        if (k, n) not in mem:
            mem[k, n] = min((L(k - 1, n//d)+ d, (k - 1, n//d, d)) for d in range(1, n+1))
        return mem[k, n][0]

    mem = {}
    score = L(K, N)
    k, n = K, N
    sol = []
    while k != 0:
        k_prev, n_prev, d = mem[k, n][1]
        print(n_prev)
        sol.append(d)
        k, n = k_prev, n_prev
    sol.reverse()
    return score, sol


if __name__ == "__main__":
    N = 12
    K = 4
    print(sum_min(K, N))
