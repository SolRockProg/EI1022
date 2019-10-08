import random
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
from typing import *
import sys
from Problemas.Sesiones1y2.LabyrinthViewer import LabyrinthViewer

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]


def load_labyrinth(filename: str) -> Tuple[Vertex, Vertex, int, int, UndirectedGraph]:
    def separa_en_tupla(linea: str) -> Tuple:
        return int(linea.split()[0]), int(linea.split()[1])

    with open(filename, "r") as f:
        vertex1 = separa_en_tupla(f.readline())
        vertex2 = separa_en_tupla(f.readline())
        x, y = separa_en_tupla(f.readline())
        aristas=[]
        for i in range(x):
            fila = f.readline().split(",")
            for j in range(y):
                letras = [("w", 0, -1), ("e", 0, 1), ("s", 1, 0), ("n", -1, 0)]
                for l, fi, co in letras:
                    if l not in fila[j]:
                        aristas.append(((i, j), (i + fi, j + co)))
    grafo=UndirectedGraph(E=aristas)
    return vertex1, vertex2, x, y, grafo


def min_saltos(grafo: UndirectedGraph, ini: tuple) -> Dict:
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


def shortest_path(g: UndirectedGraph, source: Vertex, target: Vertex) -> List[Vertex]:
    aristas = BFS(g, source, target)
    camino = backpointer(aristas, target)
    return camino


def BFS(g: UndirectedGraph, source: tuple, target: tuple) -> List[Edge]:
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

        # Comprobacion de vecinos tras los muros
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


def backpointer(aristas: list, target: tuple) -> List[Vertex]:
    dic = {v: u for (u, v) in aristas}
    camino = [target]
    while target != dic[target]:
        target = dic[target]
        camino.append(target)
    camino.reverse()
    return camino


def screen_output(wallbraker: Edge, p1: List[Vertex], p2: List[Vertex]):
    print(wallbraker[0][0], wallbraker[0][1], wallbraker[1][0], wallbraker[1][1])
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
        distances = min_saltos(g, treasure)
        wallbraker = BFS_wallbraker(g, bomb, distances)
        g.EdgeSet(g).add(wallbraker[0], wallbraker[1])
        bomb_treasure = shortest_path(g, bomb, treasure)

        # Concatenacion de caminos
        p1 = origin_treasure[:-1] + treasure_exit
        p2 = origin_bomb[:-1] + bomb_treasure[:-1] + treasure_exit

        # Salida por pantalla
        screen_output(wallbraker, p1, p2)

        if len(sys.argv) and sys.argv[2] == "-g":

            # Salida por pantalla gráfica
            random.seed(42)
            lv = LabyrinthViewer(g, canvas_width=2460, canvas_height=1000, margin=20)
            lv.add_marked_cell(treasure, 'yellow')
            lv.add_marked_cell(bomb, 'gray')
            lv.add_marked_cell(wallbraker[0], 'red', fillCell=True)
            lv.add_marked_cell(wallbraker[1], 'red', fillCell=True)
            lv.add_path(p1, 'green', -2)
            lv.add_path(p2, 'blue', 2)
            lv.run()
