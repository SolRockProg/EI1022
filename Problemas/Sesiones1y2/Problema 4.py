from algoritmia.datastructures.digraphs import UndirectedGraph
from Utils.graph2dviewer import Graph2dViewer
from Problemas.Sesiones1y2.Problema2 import DFS, backpointer
from Problemas.Sesiones1y2.Problema3 import anchura
from typing import *

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]


def cuenta_casillas(g: UndirectedGraph, source: Vertex) -> int:
    aristas = DFS(g, source)
    return len(aristas)


def cuenta_saltos(g: UndirectedGraph, rows: int) -> List[List[int]]:
    matriz = []
    aristas = anchura(g, (0, 0))
    for i in range(rows):
        lista = []
        for j in range(rows):
            lista.append(len(backpointer(aristas, (i, j))))
        matriz.append(lista)
    return matriz


def horse_graph(rows: int, cols: int) -> UndirectedGraph:
    vertices = [(u, v) for u in range(rows) for v in range(cols)]
    edges = []
    for (u, v) in vertices:
        for (ir, ic) in [(-2, 1), (-2, -1), (-1, 2), (-1, -2)]:
            if u + ir >= 0 and 0 <= v + ic < cols:
                edges.append(((u, v), (u + ir, v + ic)))

    g = UndirectedGraph(E=edges, V=vertices)
    return g


if __name__ == "__main__":
    cols = 3
    rows = 3
    g = horse_graph(rows, cols)
    source = (0, 0)
    #print(cuenta_saltos(g, rows))
    print("Hay " + str(cuenta_casillas(g, source)) + " casillas alcanzables desde " + str(source))
    viewer = Graph2dViewer(g, vertexmode=Graph2dViewer.ROW_COL)
    viewer.run()
