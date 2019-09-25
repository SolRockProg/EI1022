import random
from Utils.labyrinthviewer import LabyrinthViewer
from algoritmia.datastructures.digraphs import UndirectedGraph
from Problemas.Sesiones1y2.Laberinto import create_labyrinth


def path (g, source ,target):
    aristas=DFS(g, source)
    camino=backpointer(aristas, target)
    return camino

def backpointer(aristas, target):
    dic={v:u for (u,v) in aristas}
    v=target
    camino=[]
    camino.append(v)
    while v != dic[v]:
        v=dic[v]
        camino.append(v)
    return camino.reverse()

def DFS(g, v_inicial):
    def recursivo(u, v):
        visitados.add(v)
        aristas.append((u,v))
        for suc in g.succs(v):
           if not suc in visitados:
               recursivo(v, suc)
    visitados=set()
    aristas=[]
    recursivo(v_inicial, v_inicial)
    return aristas

if __name__ =="__main__":
    rows=100
    cols=100
    target=(rows-1, cols-1)
    source=(0,0)
    random.seed(42)
    lab = create_labyrinth(40, 60)
    viewer = LabyrinthViewer(lab, canvas_width=640, canvas_height=4680, margin=10)
    viewer.run()