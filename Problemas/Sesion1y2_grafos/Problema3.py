import random
from Utils.labyrinthviewer import LabyrinthViewer
from algoritmia.datastructures.digraphs import UndirectedGraph
from Problemas.Sesion1y2_grafos.Laberinto import create_labyrinth
from algoritmia.datastructures.queues import Fifo
from Problemas.Sesion1y2_grafos.Problema2 import backpointer, path


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
        for suc in g.succs(v):
            if suc not in visitados:
                visitados.add(suc)
                aristas.append((v, suc))
                queue.push((v, suc))
    return aristas


if __name__ == "__main__":
    rows = 80
    cols = 140
    target = (79, 139)
    source = (0, 0)
    random.seed(42)
    lab = create_labyrinth(rows, cols, n=1000)
    solucion = shortest_path(lab, source, target)
    solucion2 = path(lab, source, target)
    viewer = LabyrinthViewer(lab, canvas_width=2560, canvas_height=1080, margin=10)
    viewer.add_path(solucion, "red", -2)
    viewer.add_path(solucion2, "blue", 2)
    viewer.run()
