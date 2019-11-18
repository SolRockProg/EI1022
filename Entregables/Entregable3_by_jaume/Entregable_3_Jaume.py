from Utils.bt_scheme import PartialSolution, State, Solution, BacktrackingSolver
from typing import *
import sys
from time import time


def leeFicheroPuzles(fichero):
    for linea in open(fichero, "r", encoding="utf-8"):
        yield linea.split()

def write_solution(solution, problema):
    suma_string = "+".join(problema[:-1])
    suma_string += " = " + problema[-1] + " => "
    if len(solution) == 1:
        sol = solution[0]
        suma_list = []
        for word in problema:
            string = ""
            for letter in word:
                string += str(sol[letter])
            suma_list.append(string)
        suma_string += "+".join(suma_list[:-1])
        suma_string += " = " + suma_list[-1]
        print(suma_string)
    else:
        print(suma_string + str(len(solution)) + " soluciones")

def muestraSolucion(sol: list, linea: list):
    lon = len(sol)
    if lon == 1:
        sol = sol[0]
        cadena1 = ""
        cadena2 = ""
        for n, pal in enumerate(linea[:-1]):
            for let in pal:
                cadena2 += str(sol[let])
            if n < len(linea) - 2:
                cadena1 += pal + "+"
                cadena2 += "+"
            else:
                cadena1 += pal

        cadena1 += " = " + linea[-1] + " =>"
        cadena2 += " = "
        for let in linea[-1]:
            cadena2 += str(sol[let])
        print(cadena1, cadena2)
    else:
        cadena1 = ""
        for n, pal in enumerate(linea[:-1]):
            if n < len(linea) - 2:
                cadena1 += pal + "+"
            else:
                cadena1 += pal
        cadena1 += " = " + linea[-1] + " => "
        print(cadena1, "{} soluciones".format(lon))


def mat_letras(palabras: list):
    max_l = len(palabras[-1])
    matriz=[]
    letras= []
    for i in range(1, max_l + 1):
        fila = []
        for palabra in palabras:
            if (i - 1) < len(palabra):
                letra=palabra[-i]
                fila.append(letra)
                if letra not in letras:
                    letras.append(letra)
        matriz.append(fila)
    return matriz,letras



    #return [[palabra[-i] ]


def inicio(letra, palabras) -> int:
    for palabra in palabras:
        if letra == palabra[0]:
            return 1
    return 0


def factible(dic: dict, letras_ordenadas) -> bool:
    guardado = 0
    for l in letras_ordenadas:
        if set(l).issubset(dic.keys()):
            suma = 0
            for k in l[:-1]:
                suma += dic[k]
            suma += guardado
            guardado = suma // 10
            if l == letras_ordenadas[-1] and suma != dic[l[-1]]:
                return False
            elif suma % 10 != dic[l[-1]]:
                return False
        else:
            return True
    return True


def cryptoSolver(palabras: list):
    class CryptoAPS(PartialSolution):
        def __init__(self, asignaciones: dict):
            self.asignaciones = asignaciones
            self.vistas = len(self.asignaciones.keys())
            self.n_letras = len(letras)

        def is_solution(self) -> bool:
            # print(self.n_letras , self.vistas ,factible(palabras, self.asignaciones))
            return self.n_letras == self.vistas  # and self.factible(self.asignaciones)

        def get_solution(self) -> Solution:
            # print(self.asignaciones)
            return self.asignaciones

        def successors(self) -> Iterable["PartialSolution"]:
            if self.n_letras > self.vistas:
                l = letras[self.vistas]
                for i in range(inicio(l, palabras), 10):
                    auxdic = dict(self.asignaciones)
                    auxdic[l] = i
                    if i not in self.asignaciones.values() and factible(auxdic, letras_ordenadas):
                        yield CryptoAPS(auxdic)

    letras_ordenadas,letras = mat_letras(palabras)

    initialPS = CryptoAPS(dict())
    return BacktrackingSolver.solve(initialPS)


if __name__ == '__main__':
    # testen raras atar omitió 10 letras lol
    ini = time()
    if len(sys.argv) > 2:
        p = sys.argv[1:]
        sols = list(cryptoSolver(p))
        write_solution(sols, p)
    else:
        for linea in leeFicheroPuzles(sys.argv[1]):
            sols = list(cryptoSolver(linea))
            write_solution(sols, linea)
    fin = time()
    print(fin - ini)
