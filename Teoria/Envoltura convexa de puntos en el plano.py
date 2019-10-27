from math import atan2
from algoritmia.datastructures.queues import Lifo
from algoritmia.problems.geometry.utils import Point2D, left
from algoritmia.utils import argmax
from typing import *

def find(S: List[Point2D])-> List[int]:
    S1 = [Point2D(*i) for i in S]  # lo mismo que S1=S=[Point2D(x, y) for x,y in S]

    # Eleccion punto inicial y ordenacion
    min_y = min(p.y for p in S1)
    p = argmax((pt for pt in S1 if min_y == pt.y), lambda pt: pt.x)
    S1 = [p] + sorted((q for q in S1 if q != p), key=lambda q: (atan2(p.y - q.y, p.x - q.x), q.x))
    Q = Lifo()
    Q.push(0), Q.push(1), Q.push(2)
    for pi in range(3, len(S1)):
        pj, pk = Q[-1], Q[-2]
        while not left(S1[pk], S1[pj], S1[pi]):
            Q.pop()
            pj, pk = Q[-1], Q[-2]
        Q.push(pi)
    return [S.index(S1[Q.pop()]) for i in range(len(Q))]


S = [(2.5, 2.7), (0, 0), (1, .5), (2, -1), (2.2, 3.5), (3, 3.3), (.5, 0), (1.1, 1.4), (4, 2)]
print("Envolvente:", find(S))
