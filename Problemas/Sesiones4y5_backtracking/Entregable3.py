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
                    if self._factible(digit):
                        new_solution = deepcopy(self.solution)
                        new_solution[letters[self.n]] = digit
                        yield CryptoAPS(new_solution, self.digitos_disponibles - {digit})

        def _factible(self, digit) -> bool:
            nonlocal matrix
            acarreo = 0
            for col in range(len(matrix[0])):
                if any(matrix[fila][col] not in self.solution for fila in range(len(matrix))):
                    return True
                suma = sum(self.solution[matrix[fil][col]] for fil in range(len(matrix) - 1)) + acarreo
                acarreo = math.floor(suma/10)
                if suma != self.solution[matrix[-1][col]]:
                    return False
            return True

    matrix, letters = letters_on_strings(data)
    initial_ps = CryptoAPS({}, set(i for i in range(1, 10)))
    return BacktrackingSolver.solve(initial_ps)


def letters_on_strings(data):
    letters = []
    matrix = [[None] * len(data[-1]) for i in range(len(data))]
    for letter in range(-1, -len(data[-1]), -1):
        for word in range(len(data)):
            matrix[word][letter] = data[word][letter]
            if data[word][letter] not in letters:
                letters.append(data[word][letter])
    return matrix, tuple(letters)


if __name__ == "__main__":
    data = ("send", "more", "money")
    for sol in crypto_solver(data):
        print(sol)
