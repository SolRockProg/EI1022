import random

from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
from Utils.labyrinthviewer import LabyrinthViewer
from algoritmia.datastructures.queues import Fifo
from typing import *

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]



def read_tuple(svertex: str) -> Vertex:
    return (int(i) for i in svertex.split())

def load_laberinth(filename: str) -> Tuple[Vertex, Vertex, int, int, UndirectedGraph]:
    with open(filename, 'r') as fichero:
        tesoro= read_tuple(fichero.readline())
        bomba= read_tuple(fichero.readline())
        rows, cols = read_tuple(fichero.readline())
        vertices = [(fil, col) for fil in range(int(rows)) for col in range(int(cols))]



if __name__ == '__main__':
    load_laberinth("Ficheros/lab_4x6_2.prob")
