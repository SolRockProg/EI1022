import random

from algoritmia.datastructures.mergefindsets import *
from algoritmia.datastructures.digraphs import UndirectedGraph

from Utils.LabyrinthViewer import LabyrinthViewer


def create_labyrinth(rows, cols, n=0):
    vertexes = [(fil, col) for fil in range(rows) for col in range(cols)]
    mfs = MergeFindSet()
    for v in vertexes:
        mfs.add(v)
    edges = []
    for fil, col in vertexes:
        if fil + 1 < rows:
            edges.append(((fil, col), (fil + 1, col)))
        if col + 1 < cols:
            edges.append(((fil, col), (fil, col + 1)))
    random.shuffle(edges)
    corridors = []
    for u, v in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))
        elif n > 0:
            corridors.append((u, v))
            n -= 1
    return UndirectedGraph(E=corridors)


if __name__ == '__main__':
    random.seed(42)
    lab = create_labyrinth(40, 60)
    viewer = LabyrinthViewer(lab, canvas_width=640, canvas_height=480, margin=10)
    viewer.run()
