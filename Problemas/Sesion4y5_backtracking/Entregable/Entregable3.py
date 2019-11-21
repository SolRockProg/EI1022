import sys
from typing import *
from copy import deepcopy
from Utils.bt_scheme import BacktrackingSolver, PartialSolution, Solution
from time import time

def reader(file):
    for linea in open(file, "r", encoding="utf-8"):
        yield linea.split()


def writer(solution, problema):
    suma_string = "+".join(problema[:-1])
    suma_string += " = " + problema[-1] + " => "
    if len(solution) == 1:
        print(suma_string + solution[0])
    else:
        print(suma_string + str(len(solution)) + " soluciones")


def get_set(letter, digitos):
    return digitos - {0} if letter in last_column else digitos


def crypto_solver(data: Tuple[str, ...]) -> Iterable:
    class CryptoAPS(PartialSolution):
        def __init__(self, solution, digitos_disponibles):
            self.solution = solution
            self.n = len(solution)
            self.digitos_disponibles = digitos_disponibles

        def is_solution(self) -> bool:
            return self.n == len(letters)

        def get_solution(self) -> Solution:
            print(self.solution)
            suma_list = []
            for word in data:
                string = ""
                for letter in word:
                    string += str(self.solution[letter])
                suma_list.append(string)
            suma_string = "+".join(suma_list[:-1])
            suma_string += " = " + suma_list[-1]
            return suma_string

        def successors(self) -> Iterable["PartialSolution"]:
            if self.n < len(letters):
                new_solution = deepcopy(self.solution)
                for digit in get_set(letters[self.n], self.digitos_disponibles):
                    new_solution[letters[self.n]] = digit
                    if self._factible(new_solution):
                        yield CryptoAPS(new_solution, self.digitos_disponibles - {digit})

        def _factible(self, newsolution) -> bool:
            acarreo = 0
            for i, fila in enumerate(matrix):
                suma = 0
                for j, letra in enumerate(fila):
                    if letra not in newsolution.keys():
                        return True
                    elif j is not len(fila) - 1:
                        suma += newsolution[letra]
                suma += acarreo
                acarreo = suma // 10
                if suma % 10 != newsolution[fila[-1]]:
                    return False
                elif fila == matrix[-1] and suma != newsolution[fila[-1]]:
                    return False
            return True
    matrix = do_matrix(data)
    letters = []
    for palabra in matrix:
        for letra in palabra:
            if letra not in letters:
                letters.append(letra)
    initial_ps = CryptoAPS({}, set(i for i in range(10)))
    return BacktrackingSolver.solve(initial_ps)


def do_matrix(words):
    matrix = []
    for nletra in range(-1, -len(words[-1]) - 1, -1):
        columna = []
        for npalabra in range(len(words)):
            if nletra > -len(words[npalabra]) - 1:
                columna.append(words[npalabra][nletra])
        matrix.append(columna)
    return matrix


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Numero de argumentos incorrecto: entregable3.py <fichero | palabras>")
    elif len(sys.argv) == 2:
        start=time()
        for problema in reader(sys.argv[1]):
            last_column = [word[0] for word in problema]
            sol = list(crypto_solver(tuple(problema)))
            writer(sol, problema)
        fin=time()
        print(str(fin-start))
    else:
        problema = sys.argv[1:]
        last_column = [word[0] for word in problema]
        sol = list(crypto_solver(problema))
        writer(sol, problema)
