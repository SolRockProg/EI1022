import random

from Utils.LabyrinthViewer import LabyrinthViewer
from PruebasExamen.Tema_1_Grafos.Problema1 import create_labyrinth
from algoritmia.datastructures.queues import Fifo


def shortest_path(g, source, target):
    edges = BFS(g, source)
    return backpointer(edges, target)


def backpointer(edges, target):
    b_dict = {v: u for u, v in edges}
    res = [target]
    while target != b_dict[target]:
        target = b_dict[target]
        res.append(target)
    res.reverse()
    return res


def BFS(g, source):
    queue = Fifo()
    seen = set()
    queue.push((source, source))
    edges = []
    while len(queue) > 0:
        u, v = queue.pop()
        edges.append((u, v))
        seen.add(v)
        for suc in g.succs(v):
            if suc not in seen:
                queue.push((v, suc))
    return edges


if __name__ == "__main__":
    rows = 10
    cols = 10
    target = (rows - 1, cols - 1)
    source = (0, 0)
    random.seed(42)
    lab = create_labyrinth(rows, cols)
    solucion = shortest_path(lab, source, target)
    viewer = LabyrinthViewer(lab, canvas_width=256, canvas_height=108, margin=10)
    viewer.add_path(solucion)
    viewer.run()
