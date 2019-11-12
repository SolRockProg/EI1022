import math
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
                        yield CryptoAPS(new_solution, self.digitos_disponibles - {digit})

        def _factible(self) -> bool:
            nonlocal matrix
            acarreo = 0
            for col in range(len(matrix[0])):
                print(self.solution.keys())
                if any(matrix[fila][col] not in self.solution.keys() for fila in range(len(matrix))):
                    return True
                suma = sum(self.solution[matrix[fil][col]] for fil in range(len(matrix) - 1)) + acarreo
                acarreo = suma//10
                if suma != self.solution[matrix[-1][col]]:
                    return False
            return True

    matrix = [list(word) for word in data]
    letters = []
    for word in data:
        for character in list(word):
            if character not in letters:
                letters.append(character)
    letters = sorted(letters, key=lambda x: ())
    print(letters)
    initial_ps = CryptoAPS({}, set(i for i in range(10)))
    return BacktrackingSolver.solve(initial_ps)


if __name__ == "__main__":
    data = ("send", "more", "money")
    for sol in crypto_solver(data):
        print(sol)
