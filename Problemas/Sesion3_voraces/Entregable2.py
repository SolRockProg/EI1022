from algoritmia.datastructures.digraphs import UndirectedGraph
from typing import *
import sys
from algoritmia.utils import argmax
from time import time

from Problemas.Sesion3_voraces.graphcoloring2dviewer import GraphColoring2DViewer


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

    dic = {v: -1 for v in g.V}
    n_colores = 0
    for v in vertices:
        colores_vecinos = set()
        for vecino in g.succs(v):
            color = dic[vecino]
            if color != -1:
                colores_vecinos.add(color)
        for color in range(n_colores):
            if color not in colores_vecinos:
                dic[v] = color
                break
        else:
            dic[v] = n_colores
            n_colores += 1
    return n_colores, dic


def _vecinos_pintados(g: UndirectedGraph, vertices: set, dic: dict)->dict:
    resultado = dict()
    for v in vertices:
        n = 0  # numero de vecinos pintados
        colores = set()
        for vecino in g.succs(v):
            color = dic[vecino]
            if color != -1:
                colores.add(color)
                n += 1
        resultado[v] = n, colores

    return resultado


def _old_vecinos_pintados(g: UndirectedGraph, v, dic: dict):
    return len([i for i in g.succs(v) if dic[i] != -1])


def algoritmo2(g: UndirectedGraph) -> Tuple[int, Dict[Tuple[int, int], int]]:
    vertices = set()
    for v in g.V:
        vertices.add(v)
    dic = {v: -1 for v in g.V}
    n_colores = 0
    while len(vertices) > 0:
        vecinos=_vecinos_pintados(g, vertices, dic)
        v = argmax(vertices, fn=lambda x: (vecinos[x][0], len(g.succs(x)), x[0], x[1]))
        colores_vecinos = vecinos[v][1]
        # v = argmax(vertices, fn=lambda x: (_old_vecinos_pintados(g,x,dic), len(g.succs(x)), x[0], x[1]))
        # colores_vecinos = set()
        # for vecino in g.succs(v):
        #    color = dic[vecino]
        #    if color != -1:
        #       colores_vecinos.add(color)
        for color in range(n_colores):
            if color not in colores_vecinos:
                dic[v] = color
                break
        else:
            dic[v] = n_colores
            n_colores += 1
        vertices.remove(v)
    return n_colores, dic


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        g = load_labyrinth(sys.argv[2])
        tiempo_inicial=time()
        if sys.argv[1] == '-1':
            N, M = algoritmo1(g)
        elif sys.argv[1] == '-2':
            N, M = algoritmo2(g)
        else:
            print(sys.argv[1], "no es un argumento válido se debe poner -1 o -2")
            sys.exit(-1)
        tiempo_final = time()
        print(N)
        for v in sorted(M.keys(), key=lambda x: (x[0], x[1])):
            print(v[0], v[1], M[v])
        print("Tiempo de ejecución: ",tiempo_final-tiempo_inicial)
        if sys.argv[3] == "-g":
            viewer = GraphColoring2DViewer(g, M, window_size=(1000, 600))
            viewer.run()
    else:
        print("Uso: Entregable.py <-1 o -2> <path>")
