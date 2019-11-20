from Utils.bt_scheme import PartialSolutionWithOptimization, BacktrackingOptSolver, State, Solution
from typing import *
from random import random, seed, shuffle
from time import time
from copy import deepcopy


def binpacking(weights, capacity):
    class BinpackinPS(PartialSolutionWithOptimization):
        def __init__(self, solution, contenedores: List[int]):
            self.contenedores = contenedores
            self.solution = solution
            self.n = len(solution)

        def successors(self) -> Iterable["PartialSolutionWithOptimization"]:
            if self.n < len(weights):
                for i, weight in enumerate(self.contenedores):
                    if weight >= weights[self.n]:
                        copia = deepcopy(self.contenedores)
                        copia[i] -= weights[self.n]
                        yield BinpackinPS(self.solution + (i,), copia)
                copia = deepcopy(self.contenedores)
                copia.append(capacity - weights[self.n])
                yield BinpackinPS(self.solution + (len(self.contenedores),), copia)

        def f(self) -> Union[int, float]:
            return len(self.contenedores)

        def state(self) -> State:
            return self.n, tuple(self.contenedores)

        def is_solution(self) -> bool:
            return self.n == len(weights)

        def get_solution(self) -> Solution:
            return self.solution

    initial_ps = BinpackinPS((), [])
    return BacktrackingOptSolver.solve(initial_ps)


if __name__ == "__main__":
    W, C = [10, 20, 10, 70, 30, 60], 100
    for sol in binpacking(W, C):
        print(sol)
