from algoritmia.datastructures.digraphs import UndirectedGraph
from Utils.graph2dviewer import Graph2dViewer
from Problemas.Sesiones1y2.Problema2 import DFS, backpointer
from Problemas.Sesiones1y2.Problema3 import anchura


def cuenta_casillas(g, source):
    aristas = DFS(g, source)
    return len(aristas)


def cuenta_saltos(g, rows: int):
    matriz=[]
    aristas=anchura(g, (0,0))
    for i in range(rows):
        lista=[]
        for j in range(rows):
            lista.append(len(backpointer(aristas, (i, j)))-1)
        matriz.append(lista)
    return matriz

def horse_graph(rows, cols):
    vertices = [(u, v) for u in range(rows) for v in range(cols)]
    edges = []
    for (u, v) in vertices:
        if u - 2 >= 0 and v + 1 < cols:
            edges.append(((u, v), (u - 2, v + 1)))
        if u - 2 >= 0 and v - 1 >= 0:
            edges.append(((u, v), (u - 2, v - 1)))
        if u - 1 >= 0 and v + 2 < cols:
            edges.append(((u, v), (u - 1, v + 2)))
        if u - 1 >= 0 and v - 2 >= 0:
            edges.append(((u, v), (u - 1, v - 2)))
    g = UndirectedGraph(E=edges, V=vertices)
    return g


if __name__ == "__main__":
    cols = 10
    rows = 10
    g = horse_graph(rows, cols)
    source = (0, 0)
    print(cuenta_saltos(g, rows))
    # print("Hay "+str(cuenta_casillas(g, source))+" casillas alcanzables desde "+str(source))
    viewer = Graph2dViewer(g, vertexmode=Graph2dViewer.ROW_COL)
    viewer.run()
