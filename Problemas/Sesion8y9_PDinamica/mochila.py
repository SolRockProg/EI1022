from typing import *


# Versión recursiva directa
def mochila_rec(v: List[int], w: List[int], C: int) -> int:
    def B(n: int, u: int) -> int:
        if n == 0:
            return 0
        elif w[n - 1] <= u:
            return max(B(n - 1, u), B(n - 1, u - w[n - 1]) + v[n - 1])
        else:
            return B(n - 1, u)

    N = len(v)
    return B(N, C)


# Versión recursiva con memoización
def mochila_rec_mem(v: List[int], w: List[int], C: int) -> int:
    def B(n: int, c: int) -> int:
        if n == 0:
            return 0
        if (n, c) not in mem:
            if w[n - 1] <= c:
                mem[n, c] = max(B(n - 1, c), B(n - 1, c - w[n - 1]) + v[n - 1])
            else:
                mem[n, c] = B(n - 1, c)
        return mem[n, c]

    N = len(v)
    mem = {}
    return B(N, C)
    # Coste espacial -> O(N*C) es decir, el tamaño de mem
    # Coste temporal -> O(N*C)*0(1) que es el coste del max (coger o no coger)


# Versión recursiva con memoización y recuperación de camino
def mochila_rec_mem_camino(v: List[int], w: List[int], C: int) -> Tuple[int, List[int]]:
    def B(n: int, c: int) -> int:
        if n == 0:
            return 0
        if (n, c) not in mem:
            if w[n - 1] <= c:
                mem[n, c] = max((B(n - 1, c), (n - 1, c, 0)),
                                (B(n - 1, c - w[n - 1]) + v[n - 1], (n - 1, c - w[n - 1], 1)))
            else:
                mem[n, c] = B(n - 1, c), (n - 1, c, 0)
        return mem[n, c][0]

    N = len(v)
    mem = {}
    score = B(N, C)
    sol = []
    n, c = N, C
    while n != 0:  # Caso/s base
        sol.append(mem[n, c][1][2])
        n, c = mem[n, c][1][0], mem[n, c][1][1]
    sol.reverse()
    return score, sol


# Versión iterativa con recuperación de camino
def mochila_iter_camino(v: List[int], w: List[int], C: int) -> Tuple[int, List[int]]:
    mem = {}
    N = len(v)  # número de objetos
    for c in range(C + 1):
        mem[0, c] = 0, ()
    for n in range(1, N + 1):
        for c in range(C + 1):
            if w[n - 1] <= c:
                mem[n, c] = max((mem[n - 1, c][0], (n - 1, c, 0)),
                                (mem[n - 1, c - w[n - 1]][0] + v[n - 1], (n - 1, c - w[n - 1], 1)))
            else:
                mem[n, c] = mem[n - 1, c][0], (n - 1, c, 0)

    score = mem[N,C][0]
    sol = []
    # --------------------
    n, c = N, C
    while n != 0:  # Caso/s base
        sol.append(mem[n, c][1][2])
        n, c = mem[n, c][1][0], mem[n, c][1][1]
    sol.reverse()
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
