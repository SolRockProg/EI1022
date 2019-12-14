import contextlib
import os
import sys
from typing import *
import glob, os
from Problemas.Sesion8y9_PDinamica.Entregable.Entregable5 import *


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
    print("Prueba con: " + file2.split("\\")[-1])
    if len(vector_lineas2) != len(vector_lineas):
        print("El numero de lineas no es igual en ambos ficheros. ")
        print(file1.split("\\")[-1] + ": " + str(len(vector_lineas)) + " lineas")
        print(file2.split("\\")[-1] + ": " + str(len(vector_lineas2)) + " lineas")
    else:
        esta_bien = True
        for i, line in enumerate(vector_lineas):
            if line != vector_lineas2[i]:
                esta_bien = False
                print("Linea " + str(i) + ":\n\t+ " + str(line) + "\n\t- " + str(vector_lineas2[i]))
        if esta_bien:
            print("TODO CORRECTO")


def muchos_ficheros(f, path):
    os.chdir(path)
    for input_file in glob.glob("*.i"):
        os.system(f + " " + input_file + "> solucion.txt")
        output_file = input_file[:-1] + "o"
        comparar_ficheros("solucion.txt", output_file)


if __name__ == "__main__":
    muchos_ficheros("Entregable5.py",
                    r"C:\Users\carlo\PycharmProjects\EI1022git\Problemas\Sesion8y9_PDinamica\Entregable")
