from math import sqrt

from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo

from Utils.graph2dviewer import Graph2dViewer


def hourse_graph(rows, cols) -> UndirectedGraph:
    vertexes = [(fil, col) for fil in range(rows) for col in range(cols)]
    edges = []
    for fil, col in vertexes:
        for sr, sc in [(1, -2), (2, -1), (2, 1), (1, 2)]:
            if sr + fil < rows and 0 <= col + sc < cols:
                edges.append(((fil, col), (fil + sr, col + sc)))
    return UndirectedGraph(E=edges, V=vertexes)


def BFS_modified(g, source):
    n = int(sqrt(len(g.V)))
    matrix = [[0] * n for i in range(n)]
    queue = Fifo()
    seen = set()
    queue.push((source, 0))
    while len(queue) > 0:
        (x,y), level = queue.pop()
        matrix[x][y] = level
        seen.add((x,y))
        for suc in g.succs((x, y)):
            if suc not in seen:
                queue.push((suc, level + 1))
    return matrix


if __name__ == "__main__":
    g = hourse_graph(4, 4)
    viewer = Graph2dViewer(g, vertexmode=Graph2dViewer.ROW_COL)
    matrix = BFS_modified(g, (0, 0))
    print(matrix)

    viewer.run()
