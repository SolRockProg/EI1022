from Utils.bt_scheme import PartialSolutionWithOptimization, BacktrackingOptSolver, Solution, State
from typing import *


def coin_solver(coins, quantity):
    class CoinChangePS(PartialSolutionWithOptimization):
        def __init__(self, solution, quantity):
            self.solution = solution
            self.n = len(self.solution)
            self.quantity = quantity

        def is_solution(self) -> bool:
            return self.n == len(coins) and self.quantity == 0

        def get_solution(self) -> Solution:
            return self.solution

        def successors(self) -> Iterable["PartialSolutionWithOptimization"]:
            if self.n < len(coins):
                for decision in range(self.quantity // coins[self.n] + 1):
                    yield CoinChangePS(self.solution + (decision,), self.quantity - coins[self.n] * decision)

        def state(self) -> State:
            return self.quantity, self.n

        def f(self):
            return sum(self.solution)

    initialPS = CoinChangePS((), quantity)
    return BacktrackingOptSolver.solve(initialPS)


if __name__ == "__main__":
    coins, quantity = (1, 2, 5, 10), 11
    for sol in coin_solver(coins, quantity):
        print(sol)
