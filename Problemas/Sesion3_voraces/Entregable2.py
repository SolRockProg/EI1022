from algoritmia.datastructures.digraphs import UndirectedGraph
from typing import *
import sys
from algoritmia.utils import argmax
from algoritmia.datastructures.prioritymaps import HeapMap

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


def algoritmo2(g: UndirectedGraph) -> Tuple[int, Dict[Tuple[int, int], int]]:
    dic = {v: -1 for v in g.V}
    vertices_nocoloreados = HeapMap(opt=max, data={k: (0, len(g.succs(k)), k[0], k[1]) for k in g.V})
    n_colores = 0
    while len(vertices_nocoloreados) > 0:
        v = vertices_nocoloreados.extract_opt()
        colores_vecinos = set()
        for vecino in g.succs(v):
            color = dic[vecino]
            if color != -1:
                colores_vecinos.add(color)
            else:
                #pass
                n,s,x,y=vertices_nocoloreados[vecino]
                vertices_nocoloreados[vecino] = n+1,s,x,y
        for color in range(n_colores):
            if color not in colores_vecinos:
                dic[v] = color
                break
        else:
            dic[v] = n_colores
            n_colores += 1
    return n_colores, dic


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        g = load_labyrinth(sys.argv[2])
        if sys.argv[1] == '-1':
            N, M = algoritmo1(g)
        elif sys.argv[1] == '-2':
            N, M = algoritmo2(g)
        else:
            print(sys.argv[1], "no es un argumento válido se debe poner -1 o -2")
            sys.exit(-1)
        print(N)
        for v in sorted(M.keys(), key=lambda x: (x[0], x[1])):
            print(v[0], v[1], M[v])
        if len(sys.argv) == 4 and sys.argv[3] == "-g":
            viewer = GraphColoring2DViewer(g, M, window_size=(1000, 400))
            viewer.run()
    else:
        print("Uso: Entregable.py <-1 o -2> <path>")
