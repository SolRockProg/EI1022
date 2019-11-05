from Utils.bt_scheme import PartialSolutionWithOptimization, BacktrackingOptSolver, Solution, State
from typing import *


def coin_change_solver(coins: Tuple[int, ...], quantity: int) -> Solution:
    class CoinChangePS(PartialSolutionWithOptimization):

        def __init__(self, pending, solution=()):
            self.pending = pending
            self.solution = solution
            self.n = len(solution)

        def is_solution(self) -> bool:
            return self.n == len(coins) and self.pending == 0

        def get_solution(self) -> Solution:
            return self.solution

        def successors(self) -> Iterable["PartialSolutionWithOptimization"]:
            if self.n >= len(coins):
                return []
            for suc in range(self.pending//coins[self.n]+1):
                yield CoinChangePS(self.pending-suc*coins[self.n], self.solution+(suc,))

        def state(self) -> State:
            return self.n, self.pending

        def f(self) -> Union[int, float]:
            return sum(self.solution)

    initial_ps = CoinChangePS(quantity)
    return BacktrackingOptSolver.solve(initial_ps)


if __name__ == "__main__":
    coins, quantity = (1, 2, 5, 10), 11
    for sol in coin_change_solver(coins, quantity):
        print(sol)
