from typing import *
from random import random, seed


def mientras_quepa(W: List[int], C: int) -> List[int]:
    contenedor = 0
    c_actual = C
    res = []
    for obj in W:
        if obj <= c_actual:
            c_actual -= obj
        else:
            c_actual = C - obj
            contenedor += 1
        res.append(contenedor)
    return res


def primero_que_quepa(W: List[int], C: int) -> List[int]:
    contenedores = [C]
    res = []
    for elem in W:
        for i, c in enumerate(contenedores):
            if c >= elem:
                res.append(i)
                contenedores[i] -= elem
                break
        else:
            res.append(len(contenedores))
            contenedores.append(C - elem)
    return res


def primero_que_quepa_ordenado(W: List[int], C: int) -> List[int]:
    indexes = sorted(range(len(W)), key=lambda x: -W[x])
    contenedores = [C]
    res = [0]*len(W)
    for index in indexes:
        for i, c in enumerate(contenedores):
            if c >= W[index]:
                res[index] = i
                contenedores[i] -= W[index]
                break
        else:
            res[index]=len(contenedores)
            contenedores.append(C-W[index])
    return res


def prueba_binpacking():
    W, C = [1, 2, 8, 7, 8, 3], 10
    #seed(42)
    #W, C = [int(random()*1000)+1 for i in range(1000)], 1000
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
