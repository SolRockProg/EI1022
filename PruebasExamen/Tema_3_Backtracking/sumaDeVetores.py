from Utils.bt_scheme import PartialSolution, BacktrackingSolver, Solution
from algoritmia.datastructures.digraphs import UndirectedGraph
from typing import *


def sumandos_solver(problema: List[List[int]], S: int) -> Iterable:
    class BuscandoSumandoPS(PartialSolution):
        def __init__(self, sol: Tuple, s: int):
            self.sol = sol
            self.n = len(sol)
            self.s = s

        def is_solution(self) -> bool:
            return self.n == len(problema) and self.s == S

        def get_solution(self) -> Solution:
            return self.sol

        def successors(self) -> Iterable["PartialSolution"]:
            if self.n < len(problema):
                for elem in problema[self.n]:
                    suma = self.s + elem
                    if suma <= S:
                        yield BuscandoSumandoPS(self.sol + (elem,), suma)

    initialPS = BuscandoSumandoPS((), 0)
    return BacktrackingSolver.solve(initialPS)


if __name__ == "__main__":
    S = 16
    lista = [[4, 2], [10, 6], [8, 2]]
    for sol in sumandos_solver(lista, S):
        print(sol)
