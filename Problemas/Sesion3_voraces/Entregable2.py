from algoritmia.datastructures.digraphs import UndirectedGraph
from typing import *

from algoritmia.utils import argmax


def load_labyrinth(filename: str):
    def string_to_tuple(linea: str) -> Tuple:
        linea = linea.split()
        return (int(linea[0]), int(linea[1])), (int(linea[2]), int(linea[3]))

    with open(filename, "r") as f:
        edges = []
        for line in f:
            edges.append(string_to_tuple(line))
    graph = UndirectedGraph(E=edges)
    return graph


def algoritmo1(g: UndirectedGraph) -> Tuple[int, Dict[Tuple[int, int], int]]:
    vertices = sorted(g.V, key=lambda x: (-len(g.succs(x)), -x[0], -x[1]))
    colors = []

    dic = {v: -1 for v in g.V}
    n_colores = 0
    for v in vertices:
        colores_vecinos = set()
        for vecino in g.succs(v):
            color = dic[vecino]
            if color != -1:
                colores_vecinos.add(color)
        for color in colors:
            if color not in colores_vecinos:
                dic[v] = color
                break
        else:
            dic[v] = n_colores
            colors.append(n_colores)
            n_colores += 1
    return n_colores, dic


def _vecinos_pintados(g: UndirectedGraph, v: Tuple[int, int], dic: dict):
    return len([i for i in g.succs(v) if dic[i] != -1])


def algoritmo2(g: UndirectedGraph) -> Tuple[int, Dict[Tuple[int, int], int]]:
    vertices=set()
    for v in g.V:
        vertices.add(v)
    colors = []
    dic = {v: -1 for v in g.V}
    n_colores = 0
    while len(vertices) > 0:
        v = argmax(vertices, lambda x: (_vecinos_pintados(g, x, dic), len(g.succs(x)), x[0], x[1]))
        colores_vecinos = set()
        for vecino in g.succs(v):
            color = dic[vecino]
            if color != -1:
                colores_vecinos.add(color)
        for color in colors:
            if color not in colores_vecinos:
                dic[v] = color
                break
        else:
            dic[v] = n_colores
            colors.append(n_colores)
            n_colores += 1
        #print(v,_vecinos_pintados(g, v, dic))
        vertices.remove(v)
    return n_colores, dic


if __name__ == "__main__":
    g = load_labyrinth(
        r"C:\Users\carlo\PycharmProjects\EI1022git\Problemas\Sesion3_voraces\test-e2\graph-iberia.prob")
    N, M = algoritmo2(g)
    print(N)
    for v in M.keys():
        print(v[0], v[1], M[v])
