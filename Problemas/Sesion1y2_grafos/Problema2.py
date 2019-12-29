import random
from Utils.LabyrinthViewer import LabyrinthViewer
from algoritmia.datastructures.digraphs import UndirectedGraph
from Problemas.Sesion1y2_grafos.Laberinto import create_labyrinth


# Camino entre dos celdas de un laberinto

def path(g, source, target) -> list:
    aristas = DFS(g, source)
    camino = backpointer(aristas, target)
    return camino


def backpointer(aristas: list, target: tuple) -> list:
    dic = {v: u for (u, v) in aristas}
    camino = []
    while target != dic[target]:
        target = dic[target]
        camino.append(target)
    camino.reverse()
    return camino


def DFS(g, v_inicial):
    def recursivo(u, v):
        visitados.add(v)
        aristas.append((u, v))
        for suc in g.succs(v):
            if not suc in visitados:
                recursivo(v, suc)

    visitados = set()
    aristas = []
    recursivo(v_inicial, v_inicial)
    return aristas


if __name__ == "__main__":
    rows = 100
    cols = 100
    target = (rows - 1, cols - 1)
    source = (0, 0)
    random.seed(42)
    lab = create_labyrinth(rows, cols)
    solucion = path(lab, source, target)
    viewer = LabyrinthViewer(lab, canvas_width=2560, canvas_height=1080, margin=10)
    viewer.add_path(solucion)
    viewer.run()
