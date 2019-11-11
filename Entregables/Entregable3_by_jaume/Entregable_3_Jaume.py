import time

from bt_scheme import PartialSolution, State, Solution, BacktrackingSolver
from typing import *
import sys


def leeFicheroPuzles(fichero):
    for linea in open(fichero, "r", encoding="utf-8"):
        yield linea.split()


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


def factible(palabras: list, valores: dict) -> bool:
    max_l = max_l=len(palabras[-1])
    guardado = 0
    for i in range(1, max_l + 1):
        letras = [palabra[-i] for palabra in palabras if (i - 1) < len(palabra)]
        suma = 0
        if letras[-1] not in valores.keys():
            return True
        for k in letras[:-1]:
            if k not in valores.keys():
                return True
            suma += valores[k]
        suma += guardado
        guardado = suma // 10
        if suma % 10 != valores[letras[-1]]:
            return False
    return True


def inicio(letra, palabras) -> int:
    for palabra in palabras:
        if letra == palabra[0]:
            return 1
    return 0


def cryptoSolver(palabras: list):
    class CryptoAPS(PartialSolution):
        def __init__(self, asignaciones: dict):
            self.asignaciones = asignaciones
            self.vistas = len(self.asignaciones.keys())
            self.n_letras = len(letras)

        def is_solution(self) -> bool:
            # print(self.n_letras , self.vistas ,factible(palabras, self.asignaciones))
            return self.n_letras == self.vistas #and factible(palabras, self.asignaciones)

        def get_solution(self) -> Solution:
            # print(self.asignaciones)
            return self.asignaciones

        def successors(self) -> Iterable["PartialSolution"]:
            if self.n_letras > self.vistas:
                l = letras[self.vistas]
                for i in range(inicio(l, palabras), 10):
                    auxdic = dict(self.asignaciones)
                    auxdic[l] = i
                    if i not in self.asignaciones.values() and factible(palabras, auxdic):
                        yield CryptoAPS(auxdic)

    letras =[]
    for palabra in palabras:
        for letra in palabra:
            if letra not in letras:
                letras.append(letra)
    #letras=list({letra for palabra in palabras for letra in palabra})
    initialPS = CryptoAPS(dict())
    return BacktrackingSolver.solve(initialPS)


if __name__ == '__main__':
    tiempo = time.time()
    #testen raras atar omitió 10 letras lol
    if len(sys.argv) > 2:
        p = sys.argv[1:]
        sols = list(cryptoSolver(p))
        muestraSolucion(sols, p)
    else:
        for linea in leeFicheroPuzles(sys.argv[1]):
            sols = list(cryptoSolver(linea))
            muestraSolucion(sols, linea)
print(time.time()-tiempo)