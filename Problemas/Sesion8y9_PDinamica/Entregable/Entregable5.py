import sys


def read_file(file):
    with open(file, "r") as f:
        param = [int(val) for val in f.readline().split()]
        v = [int(val) for val in f.readline().split()]
        p = [int(val) for val in f.readline().split()]
    return param, v, p


def packing(K, C, N, v, p):
    def L(k, c, n):
        if k == 0: return 0
        if n == 0: return -float("infinity")
        if (k, c, n) not in mem:
            if p[n - 1] <= c:
                mem[k, c, n] = max((L(k - 1, c - p[n - 1], n - 1) + v[n - 1], (k - 1, c - p[n - 1], n - 1, 1)),
                                   (L(k, c, n - 1), (k, c, n - 1, 0)))
            else:
                mem[k, c, n] = (L(k, c, n - 1), (k, c, n - 1, 0))
        return mem[k, c, n][0]

    mem = {}
    score = L(K, C, N)
    k, c, n = K, C, N
    sol = []
    peso = 0
    if score != -float("infinity"):
        while k != 0:
            k_prev, c_prev, n_prev, d = mem[k, c, n][1]
            if d == 1:
                sol.append(n_prev)
                peso += p[n_prev]
            k, c, n = k_prev, c_prev, n_prev
        sol.reverse()
    return score, peso, sol


if __name__ == "__main__":
    if len(sys.argv) > 1:
        param, V, P = read_file(sys.argv[1])
        val, pes, ind = packing(*param, V, P)
        if val != -float("infinity"):
            print(val)
            print(pes)
            print(*ind, sep=" ")
        else:
            print("NO SOLUTION")
    else:
        print("número de parametros incorrecto")