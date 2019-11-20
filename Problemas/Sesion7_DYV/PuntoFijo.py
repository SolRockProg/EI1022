from typing import *

# Hacer la version recursiva

# Version iterativa
def punto_fijo(vector) -> Optional:
    indice1 = 0
    indice2 = len(vector)
    while not indice2 - indice1 == 1:
        if vector[indice1] > indice1:
            return None
        half = (indice1 + indice2) // 2
        if vector[half] > half:
            indice2 = half + 1
        elif vector[half] < half:
            indice1 = half
        else:
            return half
    return None


if __name__ == "__main__":
    vector = [-3, -2, 2, 4, 6, 10]
    print(punto_fijo(vector))
