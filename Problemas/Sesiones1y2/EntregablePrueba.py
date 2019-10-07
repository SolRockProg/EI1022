import random

from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
from Utils.labyrinthviewer import LabyrinthViewer
from algoritmia.datastructures.queues import Fifo
from typing import *

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]



def read_vertex(svertex: str) -> Vertex:
    lista = svertex.split()
    print(lista)
    vertex = (int(i) for i in lista)
    return vertex

def load_laberinth(filename: str) -> Tuple[Vertex, Vertex, int, int, UndirectedGraph]:
    with open(filename, 'r') as fichero:
        tesoro= read_vertex(fichero.readline())
        bomba= read_vertex(fichero.readline())
        rows, cols = read_vertex(fichero.readline())
        vertices = [(fil, col) for fil in range(int(rows)) for col in range(int(cols))]
        


if __name__ == '__main__':
    load_laberinth("Ficheros/lab_4x6_2.prob")
