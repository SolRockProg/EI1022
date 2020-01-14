from typing import *


def ajustar_caracteres(W: List[str], C: int):
    def P(j):
        if j == 0: return 0
        if j not in mem:
            for i in range(0, j):
                min = float("-inf")
                if j - i + 1 + sum(W[k] for k in range(i, j)) <= C:
                    aux = (P(i) + l(j - i - 1 + sum(W[k] for k in range(i, j)), C))
                    if aux < min:
                        min = aux
                mem[j] = min
        return mem[j]

    mem = {}
    score = P(len(W))
    return score

