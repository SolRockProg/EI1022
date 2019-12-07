from typing import *
from random import randrange, seed


# Versión recursiva directa
def recursos_rec(v: Dict[Tuple[int, int], int], m: List[int], U: int) -> int:
    def B(n: int, u: int) -> int:
        if n == 0: return 0
        return max(B(n - 1, u - k) + v[n - 1, k] for k in range(0, min(m[n - 1], u) + 1))

    N = len(m)
    return B(N, U)


# Versión recursiva con memoización
def recursos_rec_mem(v: Dict[Tuple[int, int], int], m: List[int], U: int) -> int:
    def B(n: int, u: int) -> int:
        if n == 0: return 0
        if (n, u) not in mem:
            mem[n, u] = max(B(n - 1, u - k) + v[n - 1, k] for k in range(0, min(m[n - 1], u) + 1))
        return mem[n, u]

    N = len(m)
    mem = {}
    return B(N, U)


# Versión recursiva con memoización y recuperación de camino
def recursos_rec_mem_camino(v: Dict[Tuple[int, int], int], m: List[int], U: int) -> Tuple[int, List[int]]:
    def B(n: int, u: int) -> int:
        if n == 0: return 0
        if (n, u) not in mem:
            mem[n, u] = max((B(n - 1, u - k) + v[n - 1, k], (n - 1, u - k, k)) for k in range(0, min(m[n - 1], u) + 1))
        return mem[n, u][0]

    N = len(m)
    mem = {}
    score = B(N, U)
    sol = []
    n, u = N, U
    while n != 0:
        _, (n_previo, u_previo, s) = mem[n, u]
        sol.append(s)
        n, u = n_previo, u_previo
    sol.reverse()
    return score, sol
    # Coste espacial -> O(N*U) es decir, el tamaño de mem.
    # Coste temporal -> O(N*C)*0(U) lo que vale el for de introducir.

# Versión iterativa con recuperación de camino
def recursos_iter_camino(v: Dict[Tuple[int, int], int], m: List[int], U: int) -> Tuple[int, List[int]]:
    mem = {}
    N = len(m)  # número de actividades
    # --------------------
    # TODO: IMPLEMENTAR rellenar tabla mem
    # --------------------

    score = 0  # TODO: cambiar por mem[N, U][0]
    sol = []
    # --------------------
    # TODO: IMPLEMENTAR recuperación de camino en sol
    # --------------------
    return score, sol


# Versión iterativa con reduccion del coste espacial
def recursos_iter_reduccion_coste(v: Dict[Tuple[int, int], int], m: List[int], U: int) -> int:
    N = len(m)
    # IMPLEMENTAR
    current = [0] * (U + 1)
    previous = [None] * (U + 1)
    # --------------------
    # TODO: IMPLEMENTAR usar dos columnas para rellenar la última de la tabla
    # --------------------
    return current[U]


# PROGRAMA PRINCIPAL -------------------------------------------------------------------------
if __name__ == "__main__":
    U = 12  # número de unidades de recurso disponibles
    m = [2, 4, 2, 4, 2]  # número máximo de recursos que podemos asignar a cada actividad
    # podemos obtener el número de actividades como len(m)
    seed(0)
    # dicionario/tabla con los beneficios que reportan asignar distintos recursos a cada actividad
    # ejemplo: v[1,3] es el beneficio que proporcionará la actividad 1 si se le asignan 3 unidades de recurso
    v = dict(((i, u), randrange(100)) for i in range(len(m)) for u in range(0, U + 1))

    print("Versión recursiva:")
    print(recursos_rec(v, m, U))
    print()
    print("Versión recursiva con memoización:")
    print(recursos_rec_mem(v, m, U))
    print()
    print("Versión recursiva con memoización y recuperación de camino:")
    print(recursos_rec_mem_camino(v, m, U))
    print()
    print("Versión iterativa con recuperación de camino:")
    print(recursos_iter_camino(v, m, U))
    print()
    print("Versión iterativa con reduccion del coste espacial:")
    print(recursos_iter_reduccion_coste(v, m, U))
