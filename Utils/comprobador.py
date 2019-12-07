import os
from typing import *


def comparar_ficheros(file1: str, file2: str):
    vector_lineas = []
    with open(file1, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                vector_lineas.append(line)
    vector_lineas2 = []
    with open(file2, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                vector_lineas2.append(line)
    if len(vector_lineas2) != len(vector_lineas):
        print("El numero de lineas no es igual en ambos ficheros. ")
        print(file1.split("\\")[-1] + ": " + str(len(vector_lineas)) + " lineas")
        print(file2.split("\\")[-1] + ": " + str(len(vector_lineas2)) + " lineas")
    else:
        for i, line in enumerate(vector_lineas):
            if line != vector_lineas2[i]:
                print("Linea " + str(i) + ":\n\t+ " + str(line) + "\n\t- " + str(vector_lineas2[i]))


if __name__ == "__main__":
    comparar_ficheros("pruebas/solucion.txt", "pruebas/pruebas.sol")
