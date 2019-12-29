from algoritmia.datastructures.digraphs import *
from algoritmia.utils import argmin


def dikstra(g: UndirectedGraph, d: WeightingFunction, v_origen, v_final):
    D = {v: float("infinity") for v in g.V}
    added = set()
    frontera = {v_origen: v_origen}
    D[v_origen] = 0
    resultado = []
    while len(frontera) > 0:
        v_destino = argmin(frontera.keys(), lambda x: D[x])
        added.add(v_destino)
        v_origen = frontera[v_destino]
        resultado.append((v_origen, v_destino))
        del frontera[v_destino]
        if v_destino == v_final:
            break
        for suc in g.succs(v_destino):
            if suc not in added and D[v_destino] + d(v_destino, suc) < D[suc]:
                frontera[suc] = v_destino
                D[suc] = D[v_destino] + d(v_destino, suc)
    return resultado


def backpointer(res, target):
    dic = {v: u for u, v in res}
    path = [target]
    while target != dic[target]:
        target = dic[target]
        path.append(target)
    path.reverse()
    return path
