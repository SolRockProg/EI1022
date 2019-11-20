from typing import *

def smax(vector: List[int], b: int, e: int) -> (int, int, int):
    if e - b == 1:
        return b, e, vector[b]
    half = (b + e) // 2
    b_izq, e_izq, acumulation_izq = smax(vector, b, half)
    b_der, e_der, acumulation_der = smax(vector, half, e)
    acumulator = 0
    max_acum_izq = vector[half-1]
    indice_izq = half-1
    for i in range(half-1, b-1, -1):
        acumulator += vector[i]
        if acumulator > max_acum_izq:
            max_acum_izq = acumulator
            indice_izq = i
    indice_der = half
    max_acum_der = vector[half]
    acumulator=0
    for i in range(half, e):
        acumulator += vector[i]
        if acumulator > max_acum_der:
            max_acum_der = acumulator
            indice_der = i+1

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
    print(vector[b:e])
    print("con un valor de: " + str(a))
