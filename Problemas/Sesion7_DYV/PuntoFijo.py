from typing import *


# Version recursiva
def punto_fijo_rec(vector: List[int], b: int, e: int) -> Optional:
    if e - b == 1:
        return b if vector[b] == b else None
    if vector[b] > b:
        return None
    half = (b + e) // 2
    if vector[half] > half:
        return punto_fijo_rec(vector, b, half)
    elif vector[half] < half:
        return punto_fijo_rec(vector, half, e)
    else:
        return half


# Version iterativa
def punto_fijo(vector: List[int]) -> Optional:
    indice1 = 0
    indice2 = len(vector)
    while not indice2 - indice1 == 1:
        if vector[indice1] > indice1:
            return None
        half = (indice1 + indice2) // 2
        if vector[half] > half:
            indice2 = half
        elif vector[half] < half:
            indice1 = half
        else:
            return half
    return indice1 if vector[indice1] == indice1 else None


if __name__ == "__main__":
    vector = [0, 2]
    print(punto_fijo(vector))
