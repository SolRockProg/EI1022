from Utils.bt_scheme import PartialSolutionWithOptimization, BacktrackingOptSolver, State, Solution
from typing import *
from random import random, seed


def knapsack_solve(weights, values, capacity):
    class KnapsackPS(PartialSolutionWithOptimization):
        def __init__(self, solution, weights, values, capacity):  # IMPLEMENTAR: Añade los parámetros que tú consideres
            self.solution = solution
            self.n = len(solution)
            self.weights = weights
            self.values = values
            self.capacity=capacity

        def is_solution(self) -> bool:  # IMPLEMENTAR
            return self.n == len(weights)

        def get_solution(self) -> Solution:  # IMPLEMENTAR
            return self.solution

        def successors(self) -> Iterable["KnapsackPS"]:  # IMPLEMENTAR
            if self.n < len(weights):
                yield KnapsackPS(self.solution+(0,), weights, values, self.capacity)
                if self.capacity >= weights[self.n]:
                    yield KnapsackPS(self.solution+(1,), weights, values, self.capacity-weights[self.n])

        def state(self) -> State:  # IMPLEMENTAR
            return self.n, self.capacity

        def f(self) -> Union[int, float]:  # IMPLEMENTAR
            return -sum(decision*values[i] for i,decision in enumerate(self.solution))

    initialPS = KnapsackPS((), weights, values, capacity)  # IMPLEMENTAR: Añade los parámetros que tú consideres
    return BacktrackingOptSolver.solve(initialPS)


def create_knapsack_problem(num_objects: int) -> Tuple[Tuple[int, ...], Tuple[int, ...], int]:
    seed(42)
    weights = [int(random() * 1000 + 1) for _ in range(num_objects)]
    values = [int(random() * 1000 + 1) for _ in range(num_objects)]
    capacity = sum(weights) // 2
    return weights, values, capacity


# Programa principal ------------------------------------------
if __name__ == "__main__":
    #W, V, C = [1, 4, 2, 3], [2, 3, 4, 2], 7  # SOLUCIÓN: Weight=7,    Value=9
    W, V, C = create_knapsack_problem(30)     # SOLUCIÓN: Weight=6313, Value=11824
    for sol in knapsack_solve(W, V, C):
        print("WEIGHT: "+str(sum(W[i]*d for i,d in enumerate(sol)))+ " VALUES: "+str(sum(V[i]*d for i,d in enumerate(sol))))
    print("\n<TERMINADO>")
