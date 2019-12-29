from Utils.bt_scheme import PartialSolution, BacktrackingSolver, Solution
from algoritmia.datastructures.digraphs import UndirectedGraph
from typing import *
from copy import deepcopy


def hamiltoniancycle_solver(g: UndirectedGraph) -> Solution:
    class HamiltonianCycle(PartialSolution):
        def __init__(self, solution: Tuple, used: Set):
            self.solution = solution
            self.n = len(solution)
            self.used = used

        def is_solution(self) -> bool:
            return self.n == len(g.V)

        def get_solution(self) -> Solution:
            return self.solution

        def successors(self) -> Iterable["PartialSolution"]:
            if self.n < len(g.V):
                for suc in g.succs(self.solution[self.n-1]):
                    if suc not in self.used:
                        new_used = deepcopy(self.used)
                        new_used.add(suc)
                        yield HamiltonianCycle(self.solution+(suc,), new_used)


    vertice = next(iter(g.V))
    usados=set()
    usados.add(vertice)
    initialPS = HamiltonianCycle((vertice,), usados)
    return BacktrackingSolver.solve(initialPS)


if __name__ == "__main__":
    G = UndirectedGraph(E=[(0, 2), (0, 3), (1, 3), (1, 4), (2, 3),
                           (2, 5), (3, 4), (3, 6), (4, 7), (5, 6),
                           (5, 8), (6, 7), (6, 8), (6, 9), (7, 9)])
    for solution in hamiltoniancycle_solver(G):
        print(solution)
