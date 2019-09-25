import random

from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
from Utils.labyrinthviewer import LabyrinthViewer

def create_labyrinth(rows, cols):
    #paso1
    vertices=[(fil, col) for fil in range(rows) for col in range(cols)]
    mfs=MergeFindSet()
    for v in vertices:
        mfs.add(v)
    edges=[]
    for (r,c) in vertices:
        if c+1<cols:
            edges.append(((r,c), (r, c+1)))
        if r+1<rows:
            edges.append(((r, c), (r+1, c)))
    random.shuffle(edges)
    corridors=[]
    #corridors.append(((2,3), (4,5)))
    for (u,v) in edges:
        if mfs.find(u) != mfs.find(v):
            corridors.append((u,v))
            mfs.merge(u, v)
    return UndirectedGraph(E=corridors)

if __name__=='__main__':
    random.seed(42)
    lab= create_labyrinth(40, 60)
    viewer= LabyrinthViewer(lab, canvas_width=640, canvas_height=4680, margin=10)
    viewer.run()