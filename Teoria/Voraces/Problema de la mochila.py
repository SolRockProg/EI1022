from typing import *


def p_mochila(pesos: List[int], precios: List[int], W: int) -> List[float]:
    indexes = sorted(range(len(precios)), key=lambda x: pesos[x] / precios[x])
    res = [0] * len(pesos)
    for i in indexes:
        res[i] = min(1, W / pesos[i])
        W -= res[i] * pesos[i]
    return res

def beneficio(precio: List[int], sol: List[float]) -> int:
    return sum(precio[i]*sol[i] for i in range(len(precio)))

if __name__ == "__main__":
    v, w, W = [60, 30, 40, 20, 75], [40, 30, 20, 10, 50], 50
    sol = p_mochila(w, v, W)
    print(sol, beneficio(v, sol))
