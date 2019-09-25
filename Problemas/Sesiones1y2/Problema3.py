import random
from Utils.labyrinthviewer import LabyrinthViewer
from algoritmia.datastructures.digraphs import UndirectedGraph
from Problemas.Sesiones1y2.Laberinto import create_labyrinth
from algoritmia.datastructures.queues import Fifo
from Problemas.Sesiones1y2.Problema2 import backpointer


# Camino más corto entre dos celdas de un laberinto modificado

def shortest_path(g, source, target):
    aristas = anchura(g, source)
    camino = backpointer(aristas, target)
    return camino


def anchura(g: UndirectedGraph, source: tuple) -> list:
    visitados = set()
    aristas = []
    queue = Fifo()
    queue.push((source, source))
    visitados.add(source)
    while len(queue) > 0:
        u, v = queue.pop()
        aristas.append((u, v))
        for suc in g.succs(v):
            if suc not in visitados:
                visitados.add(suc)
                aristas.append((v, suc))
                queue.push((v, suc))
    return aristas


if __name__ == "__main__":
    rows = 100
    cols = 100
    target = (5, 24)
    source = (3, 0)
    random.seed(42)
    lab = create_labyrinth(rows, cols, n=20)
    solucion = shortest_path(lab, source, target)
    viewer = LabyrinthViewer(lab, canvas_width=2560, canvas_height=1080, margin=10)
    viewer.add_path(solucion)
    viewer.run()
