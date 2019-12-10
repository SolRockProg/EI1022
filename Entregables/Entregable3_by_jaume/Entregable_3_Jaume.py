from Utils.bt_scheme import PartialSolution, State, Solution, BacktrackingSolver
from typing import *
import sys
from time import time


def leeFicheroPuzles(fichero):
    for linea in open(fichero, "r", encoding="utf-8"):
        yield linea.split()


def write_solution(solution, problema):
    suma_string = "+".join(problema[:-1]) + " = " + problema[-1] + " => "
    if len(solution) == 1:
        sol = solution[0]
        suma_list = []
        for word in problema:
            string = ""
            for letter in word:
                string += str(sol[letter])
            suma_list.append(string)
        suma_string += "+".join(suma_list[:-1]) + " = " + suma_list[-1]
        print(suma_string)
    else:
        print(suma_string + str(len(solution)) + " soluciones")


def mat_letras(palabras: list):
    max_l = len(palabras[-1])
    matriz = []
    letras = []
    for i in range(1, max_l + 1):
        fila = []
        for palabra in palabras:
            if (i - 1) < len(palabra):
                letra = palabra[-i]
                fila.append(letra)
                if letra not in letras:
                    letras.append(letra)
        matriz.append(fila)
    return matriz, letras


def inicio(letra, palabras) -> int:
    for palabra in palabras:
        if letra == palabra[0]:
            return 1
    return 0


def factible(dic: dict, matriz_letras) -> bool:
    guardado = 0
    for l in matriz_letras:
        suma = 0
        if l[-1] not in dic.keys():
            return True
        for k in l[:-1]:
            if k not in dic.keys():
                return True
            suma += dic[k]
        suma += guardado
        guardado = suma // 10
        if l == matriz_letras[-1] and suma != dic[l[-1]]:
            return False
        elif suma % 10 != dic[l[-1]]:
            return False
    return True


def cryptoSolver(palabras: list):
    class CryptoAPS(PartialSolution):
        def __init__(self):
            self.vistas = len(asignaciones.keys())

        def is_solution(self) -> bool:
            return n_letras == self.vistas

        def get_solution(self) -> Solution:
            return dict(asignaciones)

        def successors(self) -> Iterable["PartialSolution"]:
            if n_letras > self.vistas:
                l = letras[self.vistas]
                for i in range(inicio(l, palabras), 10):
                    if i not in numeros:
                        asignaciones[l] = i
                        if factible(asignaciones, matriz_letras):
                            numeros.add(i)
                            yield CryptoAPS()
                            numeros.remove(i)
                        del asignaciones[l]

    numeros = set()
    asignaciones = {}
    matriz_letras, letras = mat_letras(palabras)
    n_letras = len(letras)
    initialPS = CryptoAPS()
    return BacktrackingSolver.solve(initialPS)


if __name__ == '__main__':
   #t = 0
    if len(sys.argv) < 2:
        print("Numero de argumentos incorrecto: entregable3.py <fichero | palabras>")
    elif len(sys.argv) > 2:
        p = sys.argv[1:]
        sols = list(cryptoSolver(p))
        write_solution(sols, p)
    else:
        for linea in leeFicheroPuzles(sys.argv[1]):
            #ini = time()
            sols = list(cryptoSolver(linea))
            #fin = time()
            #t += (fin - ini)
            write_solution(sols, linea)
    #print(t)
