from Utils.bt_scheme import PartialSolutionWithVisitedControl, BacktrackingVCSolver, State, Solution
from typing import *


def subconjuntos_disjuntos(C, A, B):
    class SubconjuntosPS(PartialSolutionWithVisitedControl):
        def __init__(self, sa, sb, s: Set):
            self.sa = sa
            self.sb = sb
            self.s = s
            self.n = len(s)

        def successors(self) -> Iterable["PartialSolutionWithVisitedControl"]:
            if self.n > 0:
                setcopia = self.s.copy()
                elem = setcopia.pop()
                yield SubconjuntosPS(self.sa, self.sb, setcopia)
                if sum(self.sa) + elem <= A:
                    acopia = self.sa.copy()
                    acopia.add(elem)
                    yield SubconjuntosPS(acopia, self.sb, setcopia)
                if sum(self.sb) + elem <= B:
                    bcopia = self.sb.copy()
                    bcopia.add(elem)
                    yield SubconjuntosPS(self.sa, bcopia, setcopia)

        def state(self) -> State:
            return self.n, sum(self.sa), sum(self.sb)

        def is_solution(self) -> bool:
            return sum(self.sa) == A and sum(self.sb) == B

        def get_solution(self) -> Solution:
            return self.sa, self.sb

    initialPS = SubconjuntosPS(set(), set(), C)
    return BacktrackingVCSolver.solve(initialPS)


if __name__ == "__main__":
    C = {3, 1, 15, 18, 14, 23, 11, 10, 17}
    A = 50
    B = 61
    s = subconjuntos_disjuntos(C, A, B)
    print(*s, sep="")