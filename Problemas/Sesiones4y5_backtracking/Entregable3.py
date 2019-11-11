from typing import *
from copy import deepcopy

from algoritmia.utils import argmax

from Utils.bt_scheme import BacktrackingSolver, PartialSolution, Solution


def crypto_solver(data: Tuple[str, ...]) -> Iterable:
    class CryptoAPS(PartialSolution):
        def __init__(self, solution, digitos_disponibles):
            self.solution = solution
            self.n = len(solution)
            self.digitos_disponibles = digitos_disponibles

        def is_solution(self) -> bool:
            return self.n == len(letters)

        def get_solution(self) -> Solution:
            return self.solution

        def successors(self) -> Iterable["PartialSolution"]:
            if self.n < len(letters):
                for digit in self.digitos_disponibles:
                    if self._factible():
                        new_solution = deepcopy(self.solution)
                        new_solution[letters[self.n]] = digit
                        yield CryptoAPS(new_solution, self.digitos_disponibles-{digit})

        def _factible(self) -> bool:
            return True


    letters = letters_on_strings(data)
    initial_ps = CryptoAPS({}, set(i for i in range(1, 10)))
    return BacktrackingSolver.solve(initial_ps)


def letters_on_strings(data):
    letters = []
    for letter in range(-1, -len(argmax(data, lambda x: len(x))), -1):
        for word in range(len(data)):
            if data[word][letter] not in letters:
                letters.append(data[word][letter])
    return tuple(letters)


if __name__ == "__main__":
    data = ("send", "more", "money")
    for sol in crypto_solver(data):
        print(sol)
