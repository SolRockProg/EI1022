import random
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
from typing import *
import sys

from algoritmia.utils import argmin

from Problemas.Sesiones1y2.LabyrinthViewer import LabyrinthViewer

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]


def load_labyrinth(filename: str) -> Tuple[Vertex, Vertex, int, int, UndirectedGraph]:
    def string_to_tuple(linea: str) -> Tuple:
        return int(linea.split()[0]), int(linea.split()[1])

    with open(filename, "r") as f:
        vertex1 = string_to_tuple(f.readline())
        vertex2 = string_to_tuple(f.readline())
        x, y = string_to_tuple(f.readline())
        edges = []
        for i in range(x):
            fila = f.readline().split(",")
            for j in range(y):
                letters = [("w", 0, -1), ("e", 0, 1), ("s", 1, 0), ("n", -1, 0)]
                for l, row, col in letters:
                    if l not in fila[j]:
                        edges.append(((i, j), (i + row, j + col)))
    graph = UndirectedGraph(E=edges)
    return vertex1, vertex2, x, y, graph


def min_distances(g: UndirectedGraph, ini: Vertex) -> Dict:
    distances = {}
    queue = Fifo()
    seen = set()
    queue.push((ini, ini, 0))
    seen.add(ini)
    while len(queue) > 0:
        u, v, n, = queue.pop()
        distances[v] = n
        for suc in g.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v, suc, n + 1))
    return distances


def shortest_path(g: UndirectedGraph, source: Vertex, target: Vertex) -> List[Vertex]:
    aristas = BFS(g, source, target)
    path = backpointer(aristas, target)
    return path


def BFS(g: UndirectedGraph, source: Vertex, target: Vertex) -> List[Edge]:
    seen = set()
    edges = []
    queue = Fifo()
    edges.append((source, source))
    queue.push((source, source))
    seen.add(source)
    while len(queue) > 0:
        u, v = queue.pop()
        edges.append((u, v))
        if (u, v) == target:
            return edges
        for suc in g.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v, suc))
    return edges


def BFS_wallbraker(g: UndirectedGraph, source: Vertex, distances: dict) -> Edge:
    seen = set()
    min = float('infinity')
    wall = ((-1, -1), (-1, -1))
    queue = Fifo()
    queue.push((source, 0))
    seen.add(source)
    while len(queue) > 0:
        vertex, n = queue.pop()
        u, v = vertex

        # Comprobacion de vecinos tras los muros
        for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            neigh = (u + x, v + y)
            if neigh not in g.succs((u, v)) and neigh in distances:
                tdistance = n + distances[neigh]
                if tdistance < min:
                    min = tdistance
                    wall = ((u, v), neigh)
        for suc in g.succs(vertex):
            if suc not in seen:
                seen.add(suc)
                queue.push((suc, n + 1))
    return wall


def backpointer(aristas: list, target: tuple) -> List[Vertex]:
    dic = {v: u for (u, v) in aristas}
    path = [target]
    while target != dic[target]:
        target = dic[target]
        path.append(target)
    path.reverse()
    return path


def screen_output(brokenWall: Edge, p1: List[Vertex], p2: List[Vertex]):
    print(brokenWall[0][0], brokenWall[0][1], brokenWall[1][0], brokenWall[1][1])
    print(len(p1))
    print(len(p2))


if __name__ == '__main__':
    if len(sys.argv) >= 2:

        # Lectura de fichero
        lab = load_labyrinth(sys.argv[1])
        g = lab[4]
        origin = (0, 0)
        treasure = lab[0]
        bomb = lab[1]
        exit = (lab[2] - 1, lab[3] - 1)

        # Calculo de caminos sin pasar por la bomba
        origin_treasure = shortest_path(g, origin, treasure)
        treasure_exit = shortest_path(g, treasure, exit)

        # Calculo de caminos pasando por la bomba
        origin_bomb = shortest_path(g, origin, bomb)
        distances = min_distances(g, treasure)
        brokenWall = BFS_wallbraker(g, bomb, distances)
        UndirectedGraph.EdgeSet(g).add(brokenWall)
        bomb_treasure = shortest_path(g, bomb, treasure)
        treasure_exit2 = shortest_path(g, treasure, exit)

        # Concatenacion de caminos
        p1 = origin_treasure[:-1] + treasure_exit
        p2 = origin_bomb[:-1] + bomb_treasure[:-1] + treasure_exit2

        # Salida por pantalla
        screen_output(brokenWall, p1, p2)

        if len(sys.argv) and sys.argv[2] == "-g":
            # Salida por pantalla gráfica
            random.seed(42)
            lv = LabyrinthViewer(g, canvas_width=2460, canvas_height=1000, margin=20)
            lv.add_marked_cell(treasure, 'yellow')
            lv.add_marked_cell(bomb, 'gray')
            lv.add_marked_cell(brokenWall[0], 'red', fillCell=True)
            lv.add_marked_cell(brokenWall[1], 'red', fillCell=True)
            lv.add_path(p1, 'green', -2)
            lv.add_path(p2, 'blue', 2)
            lv.run()
