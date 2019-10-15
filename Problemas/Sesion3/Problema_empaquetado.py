from typing import *
from random import random, seed


def mientras_quepa(W: List[int], C: int) -> List[int]:
    contenedor = 0
    c_actual = C
    res = []
    for i in W:
        if i <= c_actual:
            c_actual -= i
        else:
            c_actual = C - i
            contenedor += 1
        res.append(contenedor)
    return res


def primero_que_quepa(W: List[int], C: int) -> List[int]:
    contenedores = {0: C}
    res = []
    for elem in W:
        fin = False
        for conte in contenedores.keys():
            if contenedores[conte] >= elem:
                contenedores[conte] -= elem
                res.append(conte)
                fin = True
                break
        if not fin:
            contenedores[len(contenedores)] = C - elem
            res.append(len(contenedores) - 1)
    return res


def primero_que_quepa_ordenado(W: List[int], C: int) -> List[int]:
    indexes = sorted(range(len(W)), key=lambda x: -x)
    contenedores = {0: C}
    res = [0] * len(W)
    for i in indexes:
        fin = False
        for conte in contenedores.keys():
            if contenedores[conte] >= W[i]:
                contenedores[conte] -= W[i]
                res[i] = conte
                fin = True
                break
        if not fin:
            contenedores[len(contenedores)] = C - W[i]
            res[i] = len(contenedores) - 1
    return res


def prueba_binpacking():
    W, C = [1, 2, 8, 7, 8, 3], 10
    # seed(42)
    # W, C = [int(random()*1000)+1 for i in range(1000)], 1000
    for solve in [mientras_quepa, primero_que_quepa, primero_que_quepa_ordenado]:
        try:
            sol = solve(W, C)
            print("-" * 40)
            print("Método:", solve.__name__)
            print("Usados {} contenedores: {}".format(1 + max(sol), sol))
        except NotImplementedError:
            print("No implementado")


if __name__ == "__main__":
    prueba_binpacking()
