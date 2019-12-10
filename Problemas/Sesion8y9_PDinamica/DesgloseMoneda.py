from typing import *


# Versión recursiva directa
def monedas_rec(v: List[int], w: List[int], m: List[int], Q: int) -> float:
    def L(q: int, n: int) -> float:
        if q == 0 and n == 0:
            return 0
        elif q > 0 and n == 0:
            return float("inf")
        else:
            return min(L(q - i * v[n - 1], n - 1) + i * w[n - 1] for i in range(0, min(m[n - 1], q // v[n - 1]) + 1))

    N = len(v)
    return L(Q, N)


# Versión recursiva con memoización
def monedas_rec_mem(v: List[int], w: List[int], m: List[int], Q: int) -> float:
    def L(q: int, n: int) -> float:
        if q == 0 and n == 0:
            return 0
        elif q > 0 and n == 0:
            return float("inf")
        else:
            if (q, n) not in mem:
                mem[q, n] = min(
                    L(q - i * v[n - 1], n - 1) + i * w[n - 1] for i in range(0, min(m[n - 1], q // v[n - 1]) + 1))
            return mem[q, n]

    mem = {}
    N = len(v)
    return L(Q, N)


# Versión recursiva con memoización y recuperación de camino
def monedas_rec_mem_camino(v: List[int], w: List[int], m: List[int], Q: int) -> Tuple[float, List[int]]:
    def L(q: int, n: int) -> float:
        if q == 0 and n == 0:
            return 0
        elif q > 0 and n == 0:
            return float("inf")
        else:
            if (q, n) not in mem:
                mem[q, n] = min(
                    (L(q - i * v[n - 1], n - 1) + i * w[n - 1], (q - i * v[n - 1], n - 1, i)) for i in
                    range(0, min(m[n - 1], q // v[n - 1]) + 1))
            return mem[q, n][0]

    mem = {}
    N = len(v)
    score = L(Q, N)
    sol = []
    n, q = N, Q
    while n != 0:
        q_previo, n_previo, d = mem[q, n][1]
        sol.append(d)
        n, q = n_previo, q_previo
    sol.reverse()
    return score, sol


# Versión iterativa con recuperación de camino
def monedas_iter_camino(v: List[int], w: List[int], m: List[int], Q: int) -> Tuple[int, List[int]]:
    pass


# Versión iterativa con reduccion del coste espacial

def monedas_iter_reduccion_coste(v: List[int], w: List[int], m: List[int], Q: int) -> int:
    # --------------------
    # TODO: IMPLEMENTAR usar dos columnas para rellenar la última de la tabla
    # --------------------
    pass


# PROGRAMA PRINCIPAL -------------------------------------------------------------------------
if __name__ == "__main__":
    Q = 24
    v = [1, 2, 5, 10]
    w = [1, 1, 4, 6]
    m = [3, 1, 4, 1]

    print("Versión recursiva:")
    print(monedas_rec(v, w, m, Q))
    print()
    print("Versión recursiva con memoización:")
    print(monedas_rec_mem(v, w, m, Q))
    print()
    print("Versión recursiva con memoización y recuperación de camino:")
    print(monedas_rec_mem_camino(v, w, m, Q))
    print()
    print("Versión iterativa con recuperación de camino:")
    print(monedas_iter_camino(v, w, m, Q))
    print()
    print("Versión iterativa con reduccion del coste espacial:")
    print(monedas_iter_reduccion_coste(v, w, m, Q))
