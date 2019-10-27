from typing import *

def monedas(lista: List[int], objetivo) -> List[int]:
    sort_list = sorted(range(len(lista)), key=lambda x: -lista[x])
    res = [0] * len(lista)
    for i in sort_list:
        res[i] = objetivo // lista[i]
        objetivo = objetivo % lista[i]
        if objetivo == 0:
            return res
    return None