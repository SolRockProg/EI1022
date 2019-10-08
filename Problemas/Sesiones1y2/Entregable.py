import random

from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
from typing import *
import sys
from Problemas.Sesiones1y2.LabyrinthViewer import LabyrinthViewer

from math import sqrt

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]

from datetime import datetime


def load_labyrinth(filename: str) -> Tuple[Vertex, Vertex, int, int, UndirectedGraph]:
    def separa_en_tupla(linea: str) -> Tuple:
        return int(linea.split()[0]), int(linea.split()[1])

    with open(filename, "r") as f:
        vertex1 = separa_en_tupla(f.readline())
        vertex2 = separa_en_tupla(f.readline())
        x, y = separa_en_tupla(f.readline())
        grafo = UndirectedGraph(V=[(u, v) for u in range(x) for v in range(y)])
        for i in range(x):
            fila = f.readline().split(",")
            for j in range(y):
                letras = [("w", 0, -1), ("e", 0, 1), ("s", 1, 0), ("n", -1, 0)]
                for l, fi, co in letras:
                    if l not in fila[j]:
                        grafo._add_edge(((i, j), (i + fi, j + co)))
    return vertex1, vertex2, x, y, grafo


def min_saltos(grafo: UndirectedGraph, ini: tuple):
    matriz = {}
    queue = Fifo()
    seen = set()
    queue.push((ini, ini, 0))
    seen.add(ini)
    while len(queue) > 0:
        u, v, n, = queue.pop()
        matriz[v] = n
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v, suc, n + 1))
    return matriz


def shortest_path(g, source, target):
    aristas = BFS(g, source, target)
    camino = backpointer(aristas, target)
    return camino


def BFS(g: UndirectedGraph, source: tuple, target: tuple) -> list:
    visitados = set()
    aristas = []
    queue = Fifo()
    aristas.append((source, source))
    queue.push((source, source))
    visitados.add(source)
    while len(queue) > 0:
        u, v = queue.pop()
        aristas.append((u, v))
        if (u, v) == target:
            return aristas
        for suc in g.succs(v):
            if suc not in visitados:
                visitados.add(suc)
                queue.push((v, suc))
    return aristas


def BFS_wallbraker(g: UndirectedGraph, source: tuple, distancias: dict) -> Edge:
    visitados = set()
    min = float('infinity')
    wall = ((-1, -1), (-1, -1))
    queue = Fifo()
    queue.push((source, 0))
    visitados.add(source)
    while len(queue) > 0:
        vertex, n = queue.pop()
        u, v = vertex
        for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            neigh = (u + x, v + y)
            if neigh not in g.succs((u, v)) and neigh in distancias:
                tdistance = n + distancias[neigh]
                if tdistance < min:
                    min = tdistance
                    wall = ((u, v), neigh)
        for suc in g.succs(vertex):
            if suc not in visitados:
                visitados.add(suc)
                queue.push((suc, n + 1))
    return wall


def backpointer(aristas: list, target: tuple) -> list:
    dic = {v: u for (u, v) in aristas}
    camino = [target]
    while target != dic[target]:
        target = dic[target]
        camino.append(target)
    camino.reverse()
    return camino


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        # tinit=datetime.now()

        lab = load_labyrinth("Ficheros/{}".format(sys.argv[1]))
        g = lab[4]
        origin = (0, 0)
        treasure = lab[0]
        bomb = lab[1]
        exit = (lab[2] - 1, lab[3] - 1)

        origin_treasure = shortest_path(g, origin, treasure)
        treasure_exit = shortest_path(g, treasure, exit)
        origin_bomb = shortest_path(g, origin, bomb)

        distances = min_saltos(g, treasure)
        wallbraker = BFS_wallbraker(g, bomb, distances)
        g._add_edge(wallbraker)
        bomb_treasure = shortest_path(g, bomb, treasure)
        # tfin = datetime.now()
        # tiempo=tfin-tinit
        # print(tiempo)

        if len(sys.argv) and sys.argv[2] =="-g":
            random.seed(42)
            graph = UndirectedGraph(E=...)
            celda1 = (1, 3)  # celdas que comparten el muro a eliminar
            celda2 = (2, 3)
            p1 = [(0, 0), (1, 0), (1, 1), ...]  # camino obtenido sin usar la bomba
            p2 = [(0, 0), (1, 0), (2, 0), ...]  # camino obtenido usando la bomba

            # ----- Poner al final del programa principal ------------
            lv = LabyrinthViewer(graph, canvas_width=1200, canvas_height=750, margin=10)
            lv.add_marked_cell(treasure, 'yellow')
            lv.add_marked_cell(bomb, 'gray')
            lv.add_marked_cell(wallbraker[0], 'red', fillCell=True)
            lv.add_marked_cell(wallbraker[1], 'red', fillCell=True)
            lv.add_path(p1, 'green', -2)
            lv.add_path(p2, 'blue', 2)
            lv.run()
