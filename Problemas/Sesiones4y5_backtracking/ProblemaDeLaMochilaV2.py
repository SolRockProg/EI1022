from Utils.bt_scheme import PartialSolutionWithOptimization, BacktrackingOptSolver, State, Solution
from typing import *
from random import random, seed
from time import time


def knapsack_solve(weights, values, capacity):
    class KnapsackPS(PartialSolutionWithOptimization):
        def __init__(self, solution=(), suma_pesos=0,
                     suma_valores=0):  # IMPLEMENTAR: Añade los parámetros que tú consideres
            self.solution = solution
            self.n = len(solution)
            self.suma_pesos = suma_pesos
            self.suma_valores = suma_valores

        def is_solution(self) -> bool:  # IMPLEMENTAR
            return self.n == len(values) and self.suma_pesos <= capacity

        def get_solution(self) -> Solution:  # IMPLEMENTAR
            return self.solution

        def successors(self) -> Iterable["KnapsackPS"]:  # IMPLEMENTAR
            if self.n >= len(values):
                return []
            yield KnapsackPS(self.solution + (0,), self.suma_pesos, self.suma_valores)
            if self.suma_pesos + weights[self.n] <= capacity:
                yield KnapsackPS(self.solution + (1,), self.suma_pesos + weights[self.n],
                                 self.suma_valores + values[self.n])

        def state(self) -> State:  # IMPLEMENTAR
            return self.n, self.suma_pesos

        def f(self) -> Union[int, float]:  # IMPLEMENTAR
            return -self.suma_valores

    initialPS = KnapsackPS()  # IMPLEMENTAR: Añade los parámetros que tú consideres
    return BacktrackingOptSolver.solve(initialPS)


def knapsack_solve2(weights, values, capacity):
    class KnapsackPS(PartialSolutionWithOptimization):
        def __init__(self, solution=()):  # IMPLEMENTAR: Añade los parámetros que tú consideres
            self.solution = solution
            self.n = len(solution)

        def is_solution(self) -> bool:  # IMPLEMENTAR
            return self.n == len(values) and suma_pesos <= capacity

        def get_solution(self) -> Solution:  # IMPLEMENTAR
            return self.solution

        def successors(self) -> Iterable["KnapsackPS"]:  # IMPLEMENTAR
            nonlocal suma_pesos
            nonlocal suma_valores
            if self.n >= len(values):
                return []
            yield KnapsackPS(self.solution + (0,))
            if suma_pesos + weights[self.n] <= capacity:
                suma_pesos += weights[self.n]
                suma_valores += values[self.n]
                yield KnapsackPS(self.solution + (1,))
                suma_pesos -= weights[self.n]
                suma_valores -= values[self.n]

        def state(self) -> State:  # IMPLEMENTAR
            return self.n, suma_pesos

        def f(self) -> Union[int, float]:  # IMPLEMENTAR
            return -suma_valores

    suma_pesos = 0
    suma_valores = 0
    initialPS = KnapsackPS()  # IMPLEMENTAR: Añade los parámetros que tú consideres
    return BacktrackingOptSolver.solve(initialPS)


def create_knapsack_problem(num_objects: int) -> Tuple[Tuple[int, ...], Tuple[int, ...], int]:
    seed(42)
    weights = [int(random() * 1000 + 1) for _ in range(num_objects)]
    values = [int(random() * 1000 + 1) for _ in range(num_objects)]
    capacity = sum(weights) // 2
    return weights, values, capacity


# Programa principal ------------------------------------------
if __name__ == "__main__":
    # W, V, C = [1, 4, 2, 3], [2, 3, 4, 2], 7  # SOLUCIÓN: Weight=7,    Value=9
    W, V, C = create_knapsack_problem(30)  # SOLUCIÓN: Weight=6313, Value=11824
    start_time = time()
    for sol in knapsack_solve(W, V, C):
        print("Weight: " + str(sum(v * W[i] for i, v in enumerate(sol))) + " Value: " + str(
            sum(v * V[i] for i, v in enumerate(sol))))
    # print(sol)
    finish_time = time()
    print("\n<TERMINADO> Tiempo de ejecucion: ", finish_time - start_time)
