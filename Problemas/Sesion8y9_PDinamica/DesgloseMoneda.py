from typing import *


# Versión recursiva directa
def monedas_rec(v: List[int], w: List[int], m: List[int], Q: int) -> float:
    def L(q: int, n: int) -> float:
        if q == 0 and n == 0:
            return 0
        elif q > 0 and n == 0:
            return float("infinity")
        else:
            return min(L(q - i * v[n - 1],n) + i * w[n - 1] for i in range(0, min(m[i], q // v[n])))

    N = len(v)
    return L(Q, N)


# Versión recursiva con memoización
def monedas_rec_mem(v: List[int], w: List[int], m: List[int], Q: int) -> int:
    pass


# Versión recursiva con memoización y recuperación de camino
def monedas_rec_mem_camino(v: List[int], w: List[int], m: List[int], Q: int) -> Tuple[int, List[int]]:
    pass


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
    m = [3, 2, 4, 1]

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
