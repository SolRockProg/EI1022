from typing import *

def acumulator_calc(inicio, fin , vector,  paso=1):
    acumulator = 0
    max_acum = vector[inicio]
    indice = inicio
    for i in range(inicio, fin, paso):
        acumulator += vector[i]
        if acumulator > max_acum:
            max_acum = acumulator
            indice = i
    return indice, max_acum

def smax(vector: List[int], b: int, e: int) -> (int, int, int):
    if e - b == 1:
        return b, e, vector[b]
    half = (b + e) // 2
    b_izq, e_izq, acumulation_izq = smax(vector, b, half)
    b_der, e_der, acumulation_der = smax(vector, half, e)
    indice_izq, max_acum_izq = acumulator_calc(half-1, b-1, vector, paso=-1)
    indice_der, max_acum_der=acumulator_calc(half, e, vector)
    best = max(acumulation_der, acumulation_izq, max_acum_izq + max_acum_der)
    if best == acumulation_izq:
        return b_izq, e_izq, acumulation_izq
    elif best == acumulation_der:
        return b_der, e_der, acumulation_der
    else:
        return indice_izq, indice_der, max_acum_der+max_acum_izq


if __name__ == "__main__":
    vector = [10, 10, 10]
    b, e, a = smax(vector, 0, len(vector))
    print("El maximo subvector encontrado es: ")
    print(vector[b:e+1])
    print("con un valor de: " + str(a))
