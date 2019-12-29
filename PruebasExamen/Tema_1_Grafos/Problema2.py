import random
from PruebasExamen.Tema_1_Grafos.Problema1 import create_labyrinth
from algoritmia.datastructures.digraphs import UndirectedGraph

from Utils.LabyrinthViewer import LabyrinthViewer


def path(g, source, target):
    edges = DFS(g, source)
    return backpointer(edges, target)


def backpointer(aristas, target):
    b_dict = {v: u for u, v in aristas}
    res = [target]
    while target != b_dict[target]:
        target = b_dict[target]
        res.append(target)
    res.reverse()
    return res


def DFS(g: UndirectedGraph, source):
    def recursivo(u, v):
        visitados.add(v)
        edges.append((u, v))
        for suc in g.succs(v):
            if suc not in visitados:
                recursivo(v, suc)

    visitados = set()
    edges = []
    recursivo(source, source)
    return edges


if __name__ == "__main__":
    rows = 10
    cols = 10
    target = (rows - 1, cols - 1)
    source = (0, 0)
    random.seed(42)
    lab = create_labyrinth(rows, cols)
    solucion = path(lab, source, target)
    viewer = LabyrinthViewer(lab, canvas_width=256, canvas_height=108, margin=10)
    viewer.add_path(solucion)
    viewer.run()
