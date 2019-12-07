from typing import *


# Versión recursiva directa
def mochila_rec(v: List[int], w: List[int], C: int) -> int:
    def B(n: int, c: int) -> int:
        if n == 0: return 0
        if w[n - 1] <= c:
            return max(B(n - 1, c), B(n - 1, c - w[n - 1]) + v[n - 1])
        else:
            return B(n - 1, c)

    N = len(v)
    return B(N, C)


# Versión recursiva con memoización
def mochila_rec_mem(v: List[int], w: List[int], C: int) -> int:
    def B(n: int, c: int) -> int:
        if n == 0: return 0
        if (n, c) not in mem:
            if w[n - 1] <= c:
                mem[n, c] = max(B(n - 1, c), B(n - 1, c - w[n - 1]) + v[n - 1])
            else:
                mem[n, c] = B(n - 1, c)
        return mem[n, c]

    N = len(v)
    mem = {}
    return B(N, C)


# Versión recursiva con memoización y recuperación de camino
def mochila_rec_mem_camino(v: List[int], w: List[int], C: int) -> Tuple[int, List[int]]:
    def B(n: int, c: int) -> int:
        if n == 0: return 0
        if (n, c) not in mem:
            if w[n - 1] <= c:
                mem[n, c] = max((B(n - 1, c), (n - 1, c, 0)),
                                (B(n - 1, c - w[n - 1]) + v[n - 1], (n - 1, c - w[n - 1], 1)))
            else:
                mem[n, c] = (B(n - 1, c), (n - 1, c, 0))
        return mem[n, c][0]

    N = len(v)
    mem = {}
    score = B(N, C)
    sol = []
    n, c = N, C
    while n != 0:
        _, (n_prev, c_prev, s) = mem[n, c]
        sol.append(s)
        n, c = n_prev, c_prev
    sol.reverse()
    return score, sol


# Versión iterativa con recuperación de camino
def mochila_iter_camino(v: List[int], w: List[int], C: int) -> Tuple[int, List[int]]:
    mem = {}
    N = len(v)  # número de objetos
    # --------------------
    # TODO: IMPLEMENTAR rellenar tabla mem
    # --------------------
    score = 0  # TODO: Cambiar por mem[N, W][0]
    sol = []
    # --------------------
    # TODO: IMPLEMENTAR recuperación de camino en sol
    # --------------------
    return score, sol


# Versión iterativa con reduccion del coste espacial

def mochila_iter_reduccion_coste(v: List[int], w: List[int], C: int) -> int:
    N = len(v)  # número de objetos
    current = [0] * (C + 1)
    previous = [None] * (C + 1)
    # --------------------
    # TODO: IMPLEMENTAR usar dos columnas para rellenar la última de la tabla
    # --------------------
    return current[C]


# PROGRAMA PRINCIPAL -------------------------------------------------------------------------
if __name__ == "__main__":
    values = [90, 75, 60, 20, 10]
    weights = [4, 3, 3, 2, 2]
    capacity = 6

    print("Versión recursiva:")
    print(mochila_rec(values, weights, capacity))
    print()
    print("Versión recursiva con memoización:")
    print(mochila_rec_mem(values, weights, capacity))
    print()
    print("Versión recursiva con memoización y recuperación de camino:")
    print(mochila_rec_mem_camino(values, weights, capacity))
    print()
    print("Versión iterativa con recuperación de camino:")
    print(mochila_iter_camino(values, weights, capacity))
    print()
    print("Versión iterativa con reduccion del coste espacial:")
    print(mochila_iter_reduccion_coste(values, weights, capacity))
