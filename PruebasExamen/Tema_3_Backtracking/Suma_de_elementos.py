from Utils.bt_scheme import PartialSolutionWithVisitedControl, BacktrackingVCSolver, State, Solution
from typing import *


def sum_solver(W: int, L: List[int]):
    class SumPS(PartialSolutionWithVisitedControl):
        def __init__(self, solution, pending):
            self.solution = solution
            self.n = len(solution)
            self.pending = pending

        def successors(self) -> Iterable["PartialSolutionWithVisitedControl"]:
            if self.n < len(L):
                if self.pending >= L[self.n]:
                    yield SumPS(self.solution + (1,), self.pending - L[self.n])
                yield SumPS(self.solution + (0,), self.pending)

        def state(self) -> State:
            return self.n, self.pending

        def is_solution(self) -> bool:
            return self.n == len(L) and self.pending == 0

        def get_solution(self) -> Solution:
            return self.solution

    initialPS = SumPS((), W)
    return BacktrackingVCSolver.solve(initialPS)
